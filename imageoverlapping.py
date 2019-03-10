import cv2
import numpy as np

img1 = cv2.imread('download.jpg')
img2 = cv2.imread('logo.png')
print (img2.shape)
print (img1.shape)


cv2.imshow('originalimg2',img2)
cv2.imshow('originalimg1',img1)

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]
#print (rows,cols,channels)
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('img2gray',img2gray)
ret,mask = cv2.threshold(img2gray,200,255,cv2.THRESH_BINARY_INV)
cv2.imshow('mask',mask)
print (ret)
#cv2.THRESH_BINARY_INV can also be used here if you want to inverse directly
mask_inv = cv2.bitwise_not(mask)
#inshort ,reversing the image colour from black to white and viceversa
cv2.imshow('mask_inv',mask_inv)
#simply getting the original image copy
print (mask_inv.shape )

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
##btwise _and compares the value of the pixel and gives the result as the larger of the two
cv2.imshow('img2_fg',img2_fg)
print (img1_bg.shape)
print (img2_fg.shape)
dst = cv2.add(img1_bg,img2_fg)
print (img1_bg,img2_fg,dst)
cv2.imshow('fv',img1_bg)
cv2.imshow('dst',dst)
img1[0:rows,0:cols] = dst
cv2.imshow('res',img1)


cv2.imshow('img2_fg',img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
