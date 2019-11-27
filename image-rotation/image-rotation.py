# -*- coding: utf-8 -*-

import cv2 
import numpy as np

def rotate270(baseImage):
    width, height,channels = baseImage.shape
    rotated = np.zeros([height,width,channels],np.uint8)
    for x in range(0,height):
        for y in range(0,width):
            rotated[x,y] = baseImage[y,height-1-x]
    return rotated
image=cv2.imread("image.jpg")
rotated270=rotate270(image)
cv2.imshow("orginal",image)
cv2.imshow("Rotated270",rotated270)
cv2.waitKey(0)
cv2.destroyAllWindows()