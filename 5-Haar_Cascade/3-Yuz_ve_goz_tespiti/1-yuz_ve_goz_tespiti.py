import cv2
import numpy as np

yuz_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
goz_casc = cv2.CascadeClassifier("haarcascade_eye.xml")

kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu = kamera.read()
    gri_video = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    yuzler = yuz_casc.detectMultiScale(gri_video,1.3,5)

    for (x,y,w,h) in yuzler:
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(0,0,255),2)

        yuz_griton = gri_video[y:y+h,x:x+w]
        yuz_renkli = goruntu[y:y+h,x:x+w]
        gozler = goz_casc.detectMultiScale(yuz_griton,1.3,4)

        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(yuz_renkli,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("goruntu",goruntu)

    if cv2.waitKey(13) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()