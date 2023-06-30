from decouple import config
from social_interaction_cloud.basic_connector import BasicSICConnector
from robot import Robot

class StateMachine(object):
    def __init__(self, server_ip: str, robot_ip: str, dialogflow_language: str, dialogflow_key_file: str, dialogflow_agent_id: str):
        self.sic = BasicSICConnector(server_ip, dialogflow_language, dialogflow_key_file, dialogflow_agent_id)
        self.sic.start()
        self.robot = Robot(self.sic, server_ip, robot_ip)

    def run(self) -> None:
        try:
            self.robot.start()  # required to start the state machine
            self.sic.rest()
            self.sic.stop()
            number_of_commands = self.robot.get_number_of_commands()
            print("number of user commands: {}".format(number_of_commands))
        except Exception:
            self.sic.rest()
            self.sic.stop()
            number_of_commands = self.robot.get_number_of_commands()
            print("StateMachine Crashed, number of user commands: {}".format(number_of_commands))
    
    def stop(self) -> None:
        self.sic.stop()

if __name__ == '__main__':
    PROJECT_ID = config('PROJECT_ID')
    KEY_PATH = config('KEY_PATH')

    example = StateMachine('127.0.0.1',
                     '192.168.0.236',
                      'en-US',
                      KEY_PATH,
                      PROJECT_ID)
    example.run()
    example.stop()
