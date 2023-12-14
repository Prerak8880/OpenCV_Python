import cv2 as cv
import numpy as np
# concept is I am Reducing Blur image from the original image
img = cv.imread('Images/1.jpeg')

gaussian_blur = cv.GaussianBlur(img,(7,7),2)

sharpened1 = cv.addWeighted(img, 15.5, gaussian_blur, -14.5, 0)

cv.imshow('Image', sharpened1)

cv.waitKey(0)
