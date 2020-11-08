import cv2

img = cv2.imread("r2.jpg")
griton = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

body_casc = cv2.CascadeClassifier("haarcascade_fullbody.xml")
body = body_casc.detectMultiScale(griton,1.8,4)

for (x,y,w,h) in body:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


