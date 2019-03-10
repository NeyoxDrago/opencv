import cv2
import numpy as np

face_cascade  = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

watch_cascade = cv2.CascadeClassifier('watch-cascade.xml')
watch2_cascade = cv2.CascadeClassifier('cascade.xml')

body_cascade = cv2.CascadeClassifier('fullbody.xml')

cap =cv2.VideoCapture(0)

while True :
    _ , img = cap.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces  = face_cascade.detectMultiScale(gray)
    watches  = watch_cascade.detectMultiScale(gray,3,3)
    watches2  = watch2_cascade.detectMultiScale(gray,3,3)
    body = body_cascade.detectMultiScale(gray)

##    for (x,y,w,h) in watches:
##        cv2.rectangle(img , (x,y) , (x+w+10,y+h+10) , (255,255,0) , 2)
##    for (x,y,w,h) in watches2:
##        cv2.rectangle(img , (x,y) , (x+w+10,y+h+10) , (255,255,0) , 2)
    for (x,y,w,h) in body:
        cv2.rectangle(img , (x,y) , (x+w+10,y+h+10) , (0,0,255) , 2)
    for (x,y,w,h) in faces:
        cv2.rectangle(img , (x,y) , (x+w+10,y+h+10) , (0,255,0) , 2)
        roi_gray =gray[y:y+h,x:x+w  ]
        roi_image = img[y:y+h , x:x+h]
        cv2.imshow('dfs',roi_image)

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_image , (ex,ey) , (ex+ew,ey+eh) , (255,0,0) , 2)


    cv2.imshow('image',img)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
        
