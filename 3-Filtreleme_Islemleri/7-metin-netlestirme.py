import cv2

resim = cv2.imread("sayfa.jpg")
resim_gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

ret,th1 = cv2.threshold(resim_gri,10,255,cv2.THRESH_BINARY)
gauss = cv2.adaptiveThreshold(resim_gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,115,1)   # değerler sabit

cv2.imshow("th1",th1)
cv2.imshow("gri resim",resim_gri)
cv2.imshow("gauss",gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()