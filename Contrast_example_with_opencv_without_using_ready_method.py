# -*- coding: utf-8 -*-

import cv2
import numpy as np

def incrementContrast(img,value=1.25):
    width,height = img.shape
    newImage=np.zeros(img.shape, np.uint8)
    for i in range(width):
        for j in range(width):
            if(img[i,j]*value>255):
                newImage[i,j]=255
            elif(img[i,j]*value<0):
                newImage[i,j]=0
            else:
                newImage[i,j]=img[i,j]*value
    return newImage
    
def decreaseContrast(img,value=0.75):
    width,height = img.shape
    newImage=np.zeros(img.shape, np.uint8)
    for i in range(width):
        for j in range(width):
            if(img[i,j]*value>255):
                newImage[i,j]=255
            elif(img[i,j]*value<0):
                newImage[i,j]=0
            else:
                newImage[i,j]=img[i,j]*value
    return newImage

image=cv2.imread("image.jpg",0)
incrementedImage=incrementContrast(image,2)
decraseImage=decreaseContrast(image,0.75)

cv2.imshow("orginal",image)
cv2.imshow("incremented",incrementedImage)
cv2.imshow("decrased",decraseImage)
cv2.waitKey(0)
cv2.destroyAllWindows()