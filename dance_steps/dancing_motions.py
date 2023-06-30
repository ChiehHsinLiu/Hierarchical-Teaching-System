import qi
import sys
import argparse
import time

from disco_left import disco_left
from disco_right import disco_right
from rolling import rolling
from right_arm_up import right_arm_up
from left_arm_up import left_arm_up

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", type=str, default="192.168.0.236",
                      help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
  parser.add_argument("--port", type=int, default=9559,
                      help="Naoqi port number")
  parser.add_argument("--motion", type=str,
                      help="Motion that you want to play in format (which_arm_direction)")
  parser.add_argument("--final", type=bool,default=True,
                      help="Whether you want the robot to rest after this motion")
  args = parser.parse_args()
  print({'args': args})
  session = qi.Session()
  try:
      session.connect("tcp://" + args.ip + ":" + str(args.port))
  except RuntimeError:
    print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
            "Please check your script arguments. Run with -h option for help.")
    sys.exit(1)

  motion_list = args.motion.split(',')
  
  motion = session.service("ALMotion")
  posture_service = session.service("ALRobotPosture")    

  switcher = {
      "rolling": rolling,
      "disco_left": disco_left,
      "disco_right": disco_right,
      "right_arm_up": right_arm_up,
      "left_arm_up": left_arm_up,
  }

  time.sleep(2)
  for m in motion_list:    
    fun = switcher.get(m)
    if fun:
      fun(motion)
  # Go to rest position
  if args.final:
      posture_service.goToPosture("Stand", 1.0)