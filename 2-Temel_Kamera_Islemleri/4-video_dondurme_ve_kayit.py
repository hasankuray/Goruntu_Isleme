import cv2

kamera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
kayit = cv2.VideoWriter("kayit.avi",fourcc,20.0,(640,480))  # saniyede 20 kere bak ve boyutları


while(kamera.isOpened()):
    ret,goruntu=kamera.read()
    if ret==True:
        goruntu=cv2.flip(goruntu,0)   # görüntü ters çevrildi
        kayit.write(goruntu)
        cv2.imshow("video",goruntu)

        if cv2.waitKey(25) & 0xFF==ord('q'):
            break

kamera.release()
kayit.release()
cv2.destroyAllWindows()
