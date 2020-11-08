import cv2

# Arkaplanda hareket varsa ve biz onu görmek istemiyorsak filtreleme yaparız
# hareket olunca gösterir.

cam = cv2.VideoCapture("video.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    _,goruntu = cam.read()
    fgmask = fgbg.apply(goruntu)

    cv2.imshow("fgmask",fgmask)
    cv2.imshow("orjinal",goruntu)

    k = cv2.waitKey(25)
    if k==27:
        break

cam.release()
cv2.destroyAllWindows()