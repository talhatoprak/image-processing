# -*- coding: utf-8 -*-

import numpy as np
import cv2

img=cv2.imread("../image.jpg")
height, width = img.shape[:2]

start_row, start_col=int(height * .05), int(width * .30)

end_row, end_col=int(height * .75), int(width * .75)

cropped=img[start_row:end_row , start_col:end_col]



cv2.imshow("Kesilen", cropped)


cv2.imshow("orginal",img)
cv2.waitKey(0)
cv2.destroyAllWindows()