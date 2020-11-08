import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

yuz_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret,goruntu = kamera.read()

    griton = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    yuzler = yuz_casc.detectMultiScale(griton,1.3,4)

    for(x,y,w,h) in yuzler:
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("video",goruntu)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break


kamera.release()
cv2.destroyAllWindows()