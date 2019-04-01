# Obstacle avoidance using Deep Learning
  I have developed a RC robot car equipped with pi camera and controlled by raspberry pi 2. The image processing module is done in my laptop from the live video feed and the desired action that sholud be performed will be given to the robot.
  
  # Dependencies Required:
  # Host System
   1.imutils
   2.numpy
   3.opencv minimum v3.3
  # Rpi
   1.socketserver
   2.Rpi.GPIO
  
  Installation steps:
  1.  place the Rpi folder in the raspberry pi.
  2.  Run the video_stream.py file in the raspberry pi. using the below command
  
      `python3 video_stream.py`
      
  3.  Run the server.py file in the host system. using the below command
      
      `python server.py --prototxt model.prototxt --model model.caffemodel --confidence 0.9`
  
  4.  Now, Run the client file from Rpi. use the command.
    
      `python servercontrol.py`
      
  Pull requests are welcomed!!
  
