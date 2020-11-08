import cv2
from matplotlib import pyplot as plt

img = cv2.imread("uthred.jpg",0)
img = cv2.medianBlur(img,5)

th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)


cv2.imshow("gaussian",th1)
cv2.imshow("mean",th2)

cv2.waitKey(0)
cv2.destroyAllWindows()