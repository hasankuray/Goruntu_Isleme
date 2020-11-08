import cv2

kamera = cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 280)


while True:
    ret,goruntu= kamera.read()
    griton = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    cv2.imshow("goruntu",goruntu)
    cv2.imshow("gri",griton)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()