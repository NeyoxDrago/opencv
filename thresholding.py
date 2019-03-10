import cv2
import numpy as np

originalimg = cv2.imread('low4.png')
cv2.imshow('originalimage',originalimg)
img = cv2.cvtColor(originalimg,cv2.COLOR_BGR2GRAY)

#THRESHOLDING REGION
####ret , binary = cv2.threshold(img,12,255,cv2.THRESH_BINARY)
####ret_inv , binary_inv = cv2.threshold(img,12,255,cv2.THRESH_BINARY_INV)
####ret_ , trunc = cv2.threshold(img,20,255,cv2.THRESH_TRUNC)
####ret__ , tozero = cv2.threshold(img,20,255,cv2.THRESH_TOZERO)
####ret___ , tozero_inv = cv2.threshold(img,20,255,cv2.THRESH_TOZERO_INV)
####
####
####cv2.imshow('binary',binary)
####cv2.imshow('binary_inv',binary_inv)
####cv2.imshow('trunc',trunc)
####cv2.imshow('tozero',tozero)
####cv2.imshow('tozero_inv',tozero_inv)

#Adaptive thresholding
##gaus = cv2.adaptiveThreshold(img ,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)
##cv2.imshow('gaus',gaus)
##
##mean = cv2.adaptiveThreshold(img ,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3)
##cv2.imshow('mean',mean)

#OTSU THRESHOLDING
ret , otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
