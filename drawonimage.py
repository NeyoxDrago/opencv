import numpy as np
import cv2

image  = cv2.imread('download.jpg',cv2.IMREAD_COLOR)

cv2.line(image,(0,0),(200,0),(0,0,120),15)
cv2.rectangle(image,(20,25),(240,180),(0,255,0),10)
cv2.circle(image,(130,103),50,(255,0,0),25)

##points =np.array([[10,10],[50,25],[70,25],[62,35],[10,150],[25,14]],np.int32)
##cv2.polylines(image,[points],True,(200,200,0),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'CARRRRRRRR!!!!',(10,150),font,5,(0,0,240),5)

cv2.imshow('car',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
