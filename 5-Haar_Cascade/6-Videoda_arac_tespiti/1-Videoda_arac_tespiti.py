import cv2

vid = cv2.VideoCapture("video1.avi")
car_casc = cv2.CascadeClassifier("cars.xml")

while True:
    ret , goruntu = vid.read()
    gri_vid = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    car = car_casc.detectMultiScale(gri_vid,1.15,3)

    for (x,y,w,h) in car:
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(0,255,255),2)

    cv2.imshow("goruntu",goruntu)

    if cv2.waitKey(13) & 0xFF==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()