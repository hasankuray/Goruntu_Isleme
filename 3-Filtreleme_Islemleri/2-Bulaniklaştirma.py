import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    # Renk Filtreleme
    ret,frame = kamera.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk_kirmizi = np.array([161, 155, 84])
    yuksek_kirmizi = np.array([179, 255, 255])

    mask = cv2.inRange(hsv,dusuk_kirmizi,yuksek_kirmizi)
    son_resim = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("son",son_resim)

    # Bulanıklarştırma  ------------------------------------------------------------------------------------
    median=cv2.medianBlur(son_resim,15)
    #------------------------------------------------------------------------------------------------------

    cv2.imshow("median",median)




    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()