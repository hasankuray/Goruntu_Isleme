import cv2
import numpy as np

mavi=[255,0,0]

resim = cv2.imread("krallar.png")

replicate = cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_REFLECT101)
wrap= cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_CONSTANT,value=mavi)

cv2.imshow("orjinal",resim)
cv2.imshow("replicate",replicate)
cv2.imshow("reflect",reflect)
cv2.imshow("reflect101",reflect101)
cv2.imshow("wrap",wrap)
cv2.imshow("constant",constant)

cv2.waitKey(0)
cv2.destroyAllWindows()
