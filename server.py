from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import socket


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# server for control messages
s = socket.socket()	
port = 9999				


s.bind(('', port))		 
print "socket binded to %s" %(port) 


s.listen(5)	 
print "socket is listening"			

#object detection part

net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

fps = FPS().start()


while True:
	vs = cv2.VideoCapture('http://192.168.43.188:8000/stream.mjpg')
	ret,frame = vs.read()
	frame = imutils.resize(frame, width=400)


	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), 127.5)

	net.setInput(blob)
	detections = net.forward()


	for i in np.arange(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]

		if confidence > args["confidence"]:
			idx = int(detections[0, 0, i, 1])
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			label=''
			cv2.rectangle(frame, (startX, startY), (endX, endY),
				COLORS[idx], 2)
			y = startY - 15 if startY - 15 > 15 else startY + 15
			c, addr = s.accept()
			print 'Got connection from', addr
			if startX<w-endX:
				cv2.putText(frame, 'right', (startX, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
				c.send("right")
			elif startX>w-endX:
				cv2.putText(frame, 'left', (startX, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
				c.send("left")
			else:
				c.send("thrust")
			
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF


	if key == ord("q"):
		break


	fps.update()


fps.stop()


cv2.destroyAllWindows()
