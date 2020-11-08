import cv2
import numpy as np

resim = cv2.imread("uthred.jpg")
cv2.imshow("kral", resim)

# Pixel de olan rengin miktarını bulma ve değiştirme
print(str(resim.item(100, 100, 1)))  # 0 blue   1 green  2 red   hangi rengin o pixelde ne miktarda olduğu görülür.
resim.itemset((100, 100, 2), 255)  # 100 e 100 pixelin kırmızı değerini 255 yapar.

print("resmin boyu, eni ve renk sayısı  " + str(resim.shape))

print("resmin pixel sayısı--" + str(resim.size))

print("resmin veritipi--" + str(resim.dtype))

bolge = resim[150:200,100:200]   # y,x bileşenleri
cv2.imshow("bune", bolge)

resim[150:200,0:100]=bolge
cv2.imshow("ikili",resim)

b,g,r=cv2.split(resim)   # renklerimizi burda ayırıyoruz
resim=cv2.merge((b,g,r))   # resimi eski renklerine geri döndürüyoruz ama bu pek kullanılmaz

resim[:,:,0] = 0     # mavi rengini 0 a eşitledik yani resimdeki mavileri yok ettik



cv2.waitKey(0)
cv2.destroyAllWindows()
