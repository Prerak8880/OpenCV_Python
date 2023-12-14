import cv2 as cv
import numpy as np

img = cv.imread('Images/1.jpeg')

#Bilateral Filtering( Reduction of Noise + Preservation Of Edges)
output_bi = cv.bilateralFilter(img, 5, 6, 6)

cv.imshow('Image', output_bi)
cv.waitKey(0)
