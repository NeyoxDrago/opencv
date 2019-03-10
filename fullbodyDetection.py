import cv2
import numpy as np

body_cascade = cv2.CascadeClassifier('fullbody.xml')

img = cv2.imread('human.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
body = body_cascade.detectMultiScale(gray)

for (x,y,w,h) in body:
    cv2.rectangle(img , (x,y) , (x+w+10,y+h+10) , (0,0,255) , 2)

cv2.imshow('image',img)


if cv2.waitKey(1) & 0xFF == ord('q'):
    cap.release()
    cv2.destroyAllWindows()
        
