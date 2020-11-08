import cv2
import numpy as np

resim = cv2.imread("buyuk_krallar.jpg")
print(str(resim.shape))

cv2.putText(resim,'Hasan',(60,80),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,3,(255,255,255),1)
cv2.imshow("kral",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()