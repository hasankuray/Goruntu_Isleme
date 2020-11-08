import cv2

vid = cv2.VideoCapture("video.mp4")
body_casc = cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
    ret , goruntu = vid.read()
    gri_vid = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    body = body_casc.detectMultiScale(gri_vid,1.15,4)
    for (x,y,w,h) in body:
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(0,255,255),3)

    cv2.imshow("goruntu",goruntu)
    if cv2.waitKey(13) & 0xFF==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()