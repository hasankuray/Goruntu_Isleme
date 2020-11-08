import cv2
import numpy as np

resim= cv2.imread("uthred.jpg")

cv2.rectangle(resim,(50,10),(140,130),(0,0,255),2)   # (x,y),(x,y)
cv2.imshow("kral",resim)

resim[10:130,50:140]=(255,255,255)       # (y:y,x:x)
cv2.imshow("beyaz kral",resim)


#toplam=cv2.add
#cv2.imshow("karma",toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()