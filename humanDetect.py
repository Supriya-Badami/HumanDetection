from scipy.spatial import distance as dist
from imutils import face_utils
import numpy as np
import imutils
import time
import dlib
import cv2

detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["jaw"]

# start the video stream thread
cap=cv2.VideoCapture(0)
while True:
	ret, frame=cap.read()
	frame = imutils.resize(frame, width=650)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	objects = detect(gray, 0)
	print(objects)
	print(type(objects))
	face=0

	for x in objects:
		face=face+1
	cv2.putText(frame, "Total humans detected = "+str(face), (10,425),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		cv2.destroyAllWindows()
		cap.release()
		break
