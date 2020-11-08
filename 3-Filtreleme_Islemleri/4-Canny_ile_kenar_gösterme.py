import cv2
import numpy as np

resim = cv2.imread("uthred.jpg")

kenarlar = cv2.Canny(resim,100,200)

cv2.imshow("resim",kenarlar)

cv2.waitKey(0)
cv2.destroyAllWindows()
