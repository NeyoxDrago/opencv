import cv2
import numpy as np

image = cv2.imread('block.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,20,0.1,10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(image,(x,y),3,-1)

cv2.imshow('Corners',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
