import cv2
import numpy as np

img_rgb = cv2.imread("ana_resim.jpg")
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

nesne = cv2.imread("template.jpg",0)

h,w =nesne.shape[::1]

res = cv2.matchTemplate(img_gray,nesne,cv2.TM_CCOEFF_NORMED)
threshold = 0.75     # bir eşik değeri oluşturduk. Bu doğruluk derecesini belirler.

loc = np.where(res>threshold)

for n in zip(*loc[::-1]):   # n nesnin sol üstünü veriyor
    cv2.rectangle(img_rgb,n,(n[0]+w,n[1]+h),(0,255,0),2)
    print(n)
cv2.imshow("ula",img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()