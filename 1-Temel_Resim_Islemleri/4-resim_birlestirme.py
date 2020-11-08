import cv2
import numpy as np

resim1=cv2.imread("uthred.jpg")
resim2=cv2.imread("scofield.jpg")


satir,sutun,kanal = resim2.shape
resim1=resim1[0:249,0:194]
resim2=resim2[0:249,0:194]




print(str(resim1.shape))
print(str(resim2.shape))

toplam = cv2.addWeighted(resim1,0.6,resim2,0.4,1)
cv2.imshow("krallar",toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()