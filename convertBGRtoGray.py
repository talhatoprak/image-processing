# -*- coding: utf-8 -*-
import cv2 
import numpy as np

def convert(img):
    print(img.shape)
    width,height , channels = img.shape
    gray = np.zeros([width,height],np.uint8)
    for i  in range(width):
        for j in range(height):
            gray[i,j] =  img[i,j,0] *  0.114 + img[i,j,1] *  0.587 + img[i,j,2] * 0.299
    return gray


image = cv2.imread('image.jpg')


gray = convert(image)

cv2.imshow('Original',image)
cv2.imshow('Gray', gray)
  
cv2.waitKey(0)
cv2.destroyAllWindows()


