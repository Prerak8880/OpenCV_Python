import cv2 as cv
import numpy as np

#-------(PART-1)-----------
# Reading the image
img = cv.imread('Images/1.jpeg')

# resizing the image
# Interpolation is Cubic for best results

img_resized = cv.resize(img, None, fx=1, fy=1)



#-------(PART-2)-----------
# removing impurities from image

img_cleared = cv.medianBlur(img_resized, 3)


img_cleared = cv.edgePreservingFilter(img_cleared, sigma_s=5)

#-------(PART-3)-----------
# Bilateral Image Filtering

img_filtered = cv.bilateralFilter(img_cleared,3,10,5)

for i in range(2):
    img_filtered = cv.bilateralFilter(img_filtered,3,20,10)
    
for i in range(2):
    img_filtered = cv.bilateralFilter(img_filtered,5,30,10)
    

#-------(PART-4)-----------    
# Sharpening the image using addWeighted()

gaus = cv.GaussianBlur(img_filtered, (7,7),2)
img_sharp = cv.addWeighted(img_filtered,1.5,gaus, -0.5, 0)
img_sharp = cv.addWeighted(img_filtered,1.4,gaus, -0.2, 10)

# Displaying Images
cv.imshow('Final Image',img_sharp)
 
cv.waitKey(0)

