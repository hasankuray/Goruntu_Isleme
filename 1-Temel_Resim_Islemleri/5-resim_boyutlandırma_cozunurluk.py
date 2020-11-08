import cv2
import numpy as np

def main():
    img = cv2.imread("uthred.jpg")
    ekran_cozunurluk= 640,480   # genişlik-boy

    skala_genislik=ekran_cozunurluk[0] / img.shape[1]
    skala_boy = ekran_cozunurluk[1] / img.shape[0]
    skala = min(skala_boy,skala_genislik)

    pencere_genislik = int(skala * img.shape[1])
    pencere_boy = int(skala * img.shape[0])

    cv2.namedWindow("boyutlanabilir_pencere",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("boyutlanabilir_pencere",pencere_genislik,pencere_boy)

    cv2.imshow("boyutlanabilir_pencere",img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()