# Hierarchical Teaching System

This is a VU University Amsterdam bachelor thesis project.

To use this hierarchical teaching system, you will need the following dependencies:

1. Naoqi Python SDK (only works in Python 2.7): <http://doc.aldebaran.com/2-8/dev/python/install_guide.html>
2. The Social Interaction Cloud (SIC): <https://socialrobotics.atlassian.net/wiki/spaces/CBSR/pages/260276225/Local+Installation#Installation>

## How to run the system:
1. Run the robot-installer.jar to connect to the robot with its IP address.
2. Change directory to the sic-local file path and start services: `docker-compose up -d redis dialogflow stream_audio`
3. Start the Redis service: `redis-server --port (your port number)`
4. Replace the robot_ip in state_machine with your own IP address:

   ` StateMachine('127.0.0.1','robot_ip','en-US',KEY_PATH,PROJECT_ID)`

5. Replace KEY_PATH and PROJECT_ID in example.env.
6. Run state_machine.py.
