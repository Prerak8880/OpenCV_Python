import cv2 as cv
import numpy as np

img = cv.imread('Images/1.jpeg')
#Median Blurring
output_med = cv.medianBlur(img, 5)

cv.imshow('Image', output_med)
cv.waitKey(0)
