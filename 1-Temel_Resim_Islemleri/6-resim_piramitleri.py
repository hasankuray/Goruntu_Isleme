import cv2

resim = cv2.imread("krallar.png")

up=cv2.pyrUp(resim)
down=cv2.pyrDown(resim)

cv2.imshow("up",up)
cv2.imshow("down",down)
cv2.imshow("orjinal",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()