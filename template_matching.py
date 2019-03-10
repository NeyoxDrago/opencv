import cv2
import numpy as np

image = cv2.imread('cpu.png')
imagegray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

template = cv2.imread('templatecpu.png',0)
print (template.shape)
w , h = template.shape[::-1]
print (w,h)

res =cv2.matchTemplate(imagegray , template , cv2.TM_CCOEFF_NORMED)
print (res)
threshold  = 0.8

loc = np.where(res >= threshold)
print((*loc[::-1]))
for pt in  zip(*loc[::-1]):
    print (pt)
    cv2.rectangle(image , pt,(pt[0] + w , pt[1]+h),(0,0,255),2)

cv2.imshow('Detection', image)
#IMAGE detection doesnt works well if the size of the main-Image is changed
