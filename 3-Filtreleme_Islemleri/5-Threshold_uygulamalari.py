import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread("uthred.jpg",0)

ret, thresh1 = cv2.threshold(resim,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(resim,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(resim,127,255,cv2.THRESH_TOZERO)
ret, thresh4 = cv2.threshold(resim,127,255,cv2.THRESH_TRUNC)

basliklar = ["orjinal resim" ,"binary","binary_inv","tozero","trunc"]
resimler =[resim,thresh1,thresh2,thresh3,thresh4]

#Görselleştirme
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(resimler[i],"gray")  # 2 satır 3 sütun 1. resim
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
