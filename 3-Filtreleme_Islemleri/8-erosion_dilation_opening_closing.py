import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()

    hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)

    dusuk__mavi = np.array([94, 80, 2])
    yuksek_mavi = np.array([126, 255, 255])

    mask = cv2.inRange(hsv,dusuk__mavi,yuksek_mavi)
    son_resim = cv2.bitwise_and(goruntu,goruntu,mask=mask)
#----------------------------------------------------------------------------------
    kernel = np.ones((5,5),np.uint8)

    erosin = cv2.erode(mask,kernel,iterations=1)
    dilation = cv2.dilate(mask,kernel,iterations=1)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    cv2.imshow("erosin",erosin)       # etraftaki küçük gürültüleri yok eder.
    cv2.imshow("dilation",dilation)   # etraftaki küçük gürültüleri daha da büyütür.Resmin içinde siyah noktalar kaldıysa bunu temizlemek için kullanılır
    cv2.imshow("opening",opening)     # aradaki boşlukları almaz
    cv2.imshow("closing",closing)     # aradaki boşlukları doldurur

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()