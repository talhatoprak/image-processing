# -*- coding: utf-8 -*-
import cv2 
import numpy as np

image=cv2.imread("image.jpg",0)

def increamentBrightness(image,value):
    width,height  = image.shape
    newImage=np.zeros(image.shape,np.uint8)
    for i in range(width):
        for j in range(height):
            if(image[i,j]+value>255):
                newImage[i,j]=255
            else:
                newImage[i,j]=image[i,j]+value
    
    return newImage

def decreaseBrightness(image,value):
    width,height  = image.shape
    newImage=np.zeros(image.shape,np.uint8)
    for i in range(width):
        for j in range(height):
            if(image[i,j]-value<0):
                newImage[i,j]=0
            else:      
                newImage[i,j]=image[i,j]-value
    
    return newImage


incrasedConstructionImage=increamentBrightness(image,70)
decreaseBrightnessImage=decreaseBrightness(image,70)

cv2.imshow("Orginal Image",image)
cv2.imshow("incrasedConstructionImage +70",incrasedConstructionImage)
cv2.imshow("decreaseBrightnessImage -70",decreaseBrightnessImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
