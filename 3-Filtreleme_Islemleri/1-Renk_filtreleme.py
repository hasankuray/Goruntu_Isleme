import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,frame=kamera.read()

    #----------------------------------------------------------------------------------------------
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk_sari=np.array([5,100,100])
    yuksek_sari=np.array([40,255,255])

    dusuk_kirmizi=np.array([161,155,84])
    yuksek_kirmizi=np.array([179,255,255])

    dusuk__mavi=np.array([94,80,2])
    yuksek_mavi=np.array([126,255,255])

    dusuk_yesil=np.array([25,52,72])
    yuksek_yesil=np.array([102,255,255])

    dusuk_beyaz=np.array([0,0,140])
    yuksek_beyaz=np.array([255,255,255])

    mask = cv2.inRange(hsv,dusuk__mavi,yuksek_mavi)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    #---------------------------------------------------------------------------------------------------

    cv2.imshow("orjinal",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("hsv",hsv)
    cv2.imshow("son resim",son_resim)




    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()