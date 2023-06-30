import os
from transitions import Machine
from functools import partial
from social_interaction_cloud.basic_connector import BasicSICConnector
from managers.speech_recognition_manager import SpeechRecognitionManager
from motion_database.motion_db import MotionDB
from utils.yes_no import YESNO

class Robot(object):
    states = [
        'asleep', 
        'awake', 
        'rest', 
        'introduced', 
        'teaching_requested', 
        'learning_initial', 
        'end_teaching', 
        'process_learning', 
        'show_new_action', 
        'action_confirmation','name_new_action', 
        'learned_something'
    ]

    def __init__(self, sic: BasicSICConnector, server_ip, robot_ip):
        self.sic = sic
        self.server_ip = server_ip
        self.robot_ip = robot_ip
        self.intention_dict = {
            'answer_yes': ['yes', 'yeah', 'yea', 'ja', 'ok', 'okay', 'oke',
                           'yup', 'jep', 'aye', 'sure', 'fine', 'alright', 'all right',
                           'affirmative', 'definitely', 'certainly',
                           'by all means', 'beyond a doubt', 'without a doubt'],
            'answer_no': ['no', 'nope', 'never', 'nah', 'negative', 'unlikely']
        }
        
        self.user_model = {}
        self.number_of_commands = 0
        self.error_model = 'i dont understand'
        self.current_request = ''
        self.recognition_manager = SpeechRecognitionManager(2)
        self.machine = Machine(model=self, states=Robot.states, initial='asleep')
        
        self.motion_lst = []
        self.motion_db = MotionDB('./motionkeys.json')
    
        # Define transitions
        self.machine.add_transition(trigger='start', source='asleep', dest='awake',
                                    before='wake_up', after='introduce')
        self.machine.add_transition(trigger='introduce', source='awake', dest='introduced',
                                    before='introduction', after='request_teaching')
        self.machine.add_transition(trigger='request_teaching', source='introduced', dest='teaching_requested',
                                    before='ask_teaching', after='confirm_teaching')
        self.machine.add_transition(trigger='confirm_teaching', source='teaching_requested', dest='learning_initial',
                                    conditions='affirmative',
                                    before='ask_sequence', after='start_learning')
        self.machine.add_transition(trigger='confirm_teaching', source='teaching_requested', dest='end_teaching',
                                    unless='affirmative',
                                    after='rest')
        
        self.machine.add_transition(trigger='start_learning', source='learning_initial', dest='process_learning',
                                    before='teaching_module', after='processing')
                
        self.machine.add_transition(trigger='processing', source='process_learning', dest='show_new_action',
                                    conditions="understood_teaching", before='show_new_actions', after='request_new_action_confirm')

        self.machine.add_transition(trigger='processing', source='process_learning', dest='learning_initial',
                                    unless="understood_teaching", before='cannot_understand', after='start_learning')        
        
        self.machine.add_transition(trigger='request_new_action_confirm', source='show_new_action', dest='action_confirmation',
                                    before='ask_new_action_correct', after='confirm_new_actions')
                
        self.machine.add_transition(trigger='confirm_new_actions', source='action_confirmation', dest='learning_initial',
                                     unless='affirmative',
                                     before='ask_sequence', after='start_learning')
        
        self.machine.add_transition(trigger='confirm_new_actions', source='action_confirmation', dest='name_new_action',
                                    conditions='affirmative',
                                    before='ask_for_action_name', after='store_action_name')
        
        self.machine.add_transition(trigger='store_action_name', source='name_new_action', dest='learned_something',
                                    before='receive_action_name', after='request_teaching')
        
        self.machine.add_transition(trigger='request_teaching', source='learned_something', dest='teaching_requested',
                                    before='ask_teaching', after='confirm_teaching')
        
        self.machine.add_transition(trigger='rest', source='*', dest='asleep',
                                    before='saying_goodbye')

    def cannot_understand(self): 
        self.sic.say_animated(self.error_model)
        self.error_model = 'i dont understand'

        self.recognition_manager.reset()
        self.sic.wait(2, callback=self.ask_sequence)

    def understood_teaching(self) -> bool:
        motion_sequence = self.user_model.get(self.current_request)

        if not isinstance(motion_sequence, list):
            return False
        
        for action_key in motion_sequence:
            action_values = self.motion_db.get(action_key)

            if not action_values:
                self.error_model = "i dont unserstand {}".format(action_key)
                return False

        return True

    def wake_up(self) -> None:
        self.sic.set_language('en-US')
        self.sic.wake_up()
        self.sic.run_loaded_actions()

    def introduction(self) -> None:
        self.sic.say('Hi, I am Nao, you can teach me new dance with the dancing steps I already know!')
        
    def saying_thanks(self) -> None:
        self.sic.say_animated('Thank you!')
        
    def saying_goodbye(self) -> None:
        self.sic.say('Goodbye!')
        self.sic.rest()
        
    def ask_teaching(self) -> None:
        self.current_request = 'chain_request'
    
        while not self.recognition_manager.success and self.recognition_manager.attempts <= 2:
            self.sic.say('Do you want to teach me new dancing steps?')
            self.sic.speech_recognition_shortcut('answer_yesno', self.intention_dict, 8,
                                                  callback=partial(self.on_yesno, 'chain_request'))

        self.recognition_manager.reset()
        
    def on_yesno(self, user_model_id: str, detection_result) -> None:
        self.number_of_commands += 1
        answer = ''
        if isinstance(detection_result, dict):
            if detection_result and 'intent' in detection_result and detection_result['intent']:
                answer = detection_result['intent']
        elif isinstance(detection_result, str):
            answer = detection_result
        
        if answer:
            if answer == 'answer_no':
                self.user_model[user_model_id] = YESNO.NO
                self.recognition_manager.attempt_succeeded()
            elif answer == 'answer_yes':
                self.user_model[user_model_id] = YESNO.YES
                self.recognition_manager.attempt_succeeded()
        else:
            self.recognition_manager.attempt_failed()
            
    def on_entity(self, intent: str, user_model_id: str, detection_result: dict) -> None:
      
        self.number_of_commands += 1
        correct_intent = detection_result and 'intent' in detection_result and detection_result['intent'] == intent
        user_model = detection_result and 'parameters' in detection_result and user_model_id in detection_result['parameters']
        
        result = user_model and detection_result['parameters'][user_model_id]
        print({"detection_result": detection_result, "result": result, "correct_intent": correct_intent, 'user_model': user_model})
        
        if  correct_intent and user_model and result:
            self.user_model[user_model_id] = result
            self.recognition_manager.attempt_succeeded()
        else:
            self.recognition_manager.attempt_failed()
            
    def ask_sequence(self) -> None:
        print('start ask_sequence')
        self.sic.say('Could you tell me the dance sequence')
        self.current_request = "ask_sequence"
        self.user_model[self.current_request] = ''
        self.recognition_manager.reset()

    def show_new_actions(self):
        self.motion_lst = list(map(lambda x: x.replace(' ', '_'), self.user_model[self.current_request]))        
        for action_key in self.motion_lst:
            action_values = self.motion_db.get(action_key)
            if isinstance(action_values, list):
                chain_index = self.motion_lst.index(action_key)
                self.motion_lst[chain_index] = action_values

                temp_lst = []
                for i in self.motion_lst:
                    if isinstance(i,list):
                        temp_lst += i
                    else:
                        temp_lst += [i]
                        
                self.motion_lst = temp_lst     
        
        motion_str_lst = ','.join(self.motion_lst)

        if motion_str_lst:
            os.system('python2.7 ./dance_steps/dancing_motions.py --ip {ip} --motion {motion}'.format(ip=self.robot_ip, motion=motion_str_lst))
    
    def ask_new_action_correct(self) -> None:
        self.current_request = "correct_chain"
        self.sic.say('Is my dancing correct?')
        self.sic.speech_recognition_shortcut('answer_yesno', self.intention_dict, 3,
                                                  callback=partial(self.on_yesno, 'correct_chain'))
        
    def ask_for_action_name(self) -> None:
        self.current_request = "answer_dance_name"
        self.ask_entity_question('What is the name of this dance?', 'answer_dance_name',
                                 ["step one", "step two", "step three", "step four", "step five", "step six", "step seven", "step eight", "step nine", "step ten", "new dance"], 'answer_dance_name', 8, 8)

    def on_entity_touch(self, user_model_id: str, entity):
        self.number_of_commands += 1
        if entity:
            self.user_model[user_model_id] = entity
  
    def ask_entity_question(self, question: str, user_model_id: str, entity_shortcut: list,
                            context: str, speech_duration: int, touch_duration: int, max_speech_attempts: int = 2):
        self.recognition_manager.reset()
        self.recognition_manager.max_attempts = max_speech_attempts
        if user_model_id in self.user_model:
            del self.user_model[user_model_id]
       
        while self.recognition_manager.can_recognize():
            self.sic.say(question)
            self.sic.speech_recognition(context, speech_duration, partial(self.on_entity, context, user_model_id))

        if not self.recognition_manager.success:
            self.sic.say('Whoops, I did not quite get that.')
            self.sic.say('I will call out a few answer options.')
            self.sic.say('Press my toe under the green light to select an answer.')
            self.sic.say('And optionally press the toe under the red light to move to the next option.')

            self.sic.set_led_color(['RightFootLeds', 'LeftFootLeds'], ['green', 'red'])
            
            for entity in entity_shortcut:
                self.sic.say(entity)
                self.sic.subscribe_event_listener('RightBumperPressed',
                                                partial(self.on_entity_touch, user_model_id, entity), load=True)
                self.sic.subscribe_event_listener('LeftBumperPressed',
                                                partial(self.on_entity_touch, user_model_id, ''), load=True)
                self.sic.wait(touch_duration, load=True)
                self.sic.run_loaded_actions(wait_for_any=True)
                self.sic.unsubscribe_event_listener('RightBumperPressed')
                self.sic.unsubscribe_event_listener('LeftBumperPressed')

                if user_model_id in self.user_model:
                    break

            self.sic.set_led_color(['RightFootLeds', 'LeftFootLeds'], ['off', 'off'])

        self.recognition_manager.reset()
        
    def receive_action_name(self) -> None:
        key = self.user_model[self.current_request]
        value = self.motion_lst
        print({'key': key, 'value': value})
        if isinstance(key, str):
            self.motion_db.set(key.replace(' ', '_'), value)
            self.sic.say('I learn a new dancing step, thank you!')
                            
        self.recognition_manager.reset()         
            
    def teaching_module(self) -> None:
        self.sic.speech_recognition('answer_dance_motion', 20, callback=self.receive_chain)

    def get_number_of_commands(self) -> int:
        return self.number_of_commands

    def receive_chain(self, detection_result: dict) -> None:
        self.number_of_commands += 1
        
        params = detection_result and detection_result.get('parameters')
        motion_sequence = params and params.get('motion_sequence')
        
        print({"detection_result": detection_result, "motion_sequence": motion_sequence})

        if  motion_sequence:
            self.user_model[self.current_request] = motion_sequence
            self.recognition_manager.attempt_succeeded()
        else:
            self.user_model[self.current_request] = ''
            self.recognition_manager.attempt_failed()
    
    def affirmative(self) -> bool:
        print({"current": self.current_request, "answer": self.user_model.get(self.current_request), "result": self.user_model.get(self.current_request) == YESNO.YES})
        return self.user_model.get(self.current_request) == YESNO.YES
    
    def reset_recognition_management(self) -> None:
        self.recognition_manager.reset()