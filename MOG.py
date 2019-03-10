import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fg = cv2.createBackgroundSubtractorMOG2()

try:
    while True:
        ret , frame = cap.read()
        fgmask = fg.apply(frame)

        
        #MORPHOLOGY-------------
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower = np.array([50,50,50])
        high = np.array([200,200,200])
        mask = cv2.inRange(hsv,lower,high)
        kernel  = np.ones((4,4),np.uint8)
        morph = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
        cv2.imshow('fgfsgefg' , mask)
        #-----------------------

##        blur = cv2.GaussianBlur(fgmask,(10,10),0)
##
        cv2.imshow('original',frame)
        cv2.imshow('fg' , fgmask)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()

    
except Exception as e:
    print('exit')
