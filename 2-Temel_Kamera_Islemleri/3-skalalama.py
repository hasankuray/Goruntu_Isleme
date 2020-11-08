import cv2

kamera = cv2.VideoCapture(0)

def skalalama(goruntu,yuzde=75):
    width = int(goruntu.shape[1] * yuzde / 100)
    height = int(goruntu.shape[0] * yuzde / 100)
    boyut = (width,height)
    return cv2.resize(goruntu,boyut,interpolation=cv2.INTER_AREA)


while True:
    ret,goruntu = kamera.read()
    goruntu50= skalalama(goruntu,50)
    cv2.imshow("goruntu",goruntu)
    cv2.imshow("goruntu50",goruntu50)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
