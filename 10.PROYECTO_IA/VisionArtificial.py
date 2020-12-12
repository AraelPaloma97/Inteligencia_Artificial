"""
proyecto: Visión artificial

@authors:
    LUNA GONZALES ROCIO
    MARTINEZ GARCIA ISABEL
    PALOMA VICTORIANO ARAEL
    ROBLES PADILLA OSWALDO
"""
#importando librerias 
import cv2
import numpy as np
import serial
import time
#COM3 CORESPONDE A NUESTRO SERIAL DE ARDUINO
puerto = serial.Serial('COM3',9600)
cap = cv2.VideoCapture(1)

#El color a indentificar es el rosa
while True:

	_,frame = cap.read() 
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	grayImage=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	low_rosa = np.array([130, 120, 72])
	high_rosa = np.array([160, 255, 255]) 
 
	
	height = frame.shape[0]
	width = frame.shape[1]
	channels = frame.shape[2]

	largo=height/2
	ancho=width/2
	
	output=frame.copy()
	circles=cv2.HoughCircles( grayImage,cv2.HOUGH_GRADIENT,2,4000, param1=50,param2=30,minRadius=40, maxRadius=90)
	circles=np.uint16(np.around(circles))
	for imagenrosa in circles[0,:]:
		corx=imagenrosa[0]
		cory=imagenrosa[1]
		radio=imagenrosa[2]
		cv2.circle(output,(corx,cory),radio,(50,255,50),2)
	cv2.imshow('Camaraweb',output)
	hori=int(corx)-int(ancho)
	ver=int(cory)-int(largo)
	if(hori<=0):
		puerto.write(b'n')
		time.sleep(1)
	else:
		if(hori>=0):
			puerto.write(b'r')
			time.sleep(1)
		else:
			puerto.write(b' ')
			time.sleep(1)
	if(ver<=0):
		puerto.write(b'i')
		time.sleep(1)
	else:
		if(hori>=0):
			puerto.write(b'p')
			time.sleep(1)
		else:
			puerto.write(b' ')
			time.sleep(1)
	espacio = cv2.waitKey(5) & 0xFF
	if espacio == 27:
		break   
  
rang = cv2.inRange( hsv_frame, low_rosa, high_rosa)
cv2.imshow("Formato",frame)
cv2.imshow("Image", cap)
cv2.imshow("Mask", rang)

cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
