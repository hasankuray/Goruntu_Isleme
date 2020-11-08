import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dusuk_kirmizi = np.array([161, 155, 84])
    yuksek_kirmizi = np.array([179, 255, 255])

    mask = cv2.inRange(hsv,dusuk_kirmizi,yuksek_kirmizi)
    son_resim = cv2.bitwise_and(frame,frame,mask=mask)

    #----------------------------------------------------------------------------------------------
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    sobelX = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    kenarlar= cv2.Canny(frame,100,200)
    #-----------------------------------------------------------------------------------------------
    cv2.imshow("laplacian",laplacian)
    cv2.imshow("sobelX",sobelX)
    cv2.imshow("sobely",sobely)
    cv2.imshow("kenarlar",kenarlar)


    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()