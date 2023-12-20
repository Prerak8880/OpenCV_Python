import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

  #Specifying height and width for the camera
    width = int(cap.get(3))
    height = int(cap.get(4))
  
    image = np.zeros(frame.shape, np.uint8)   #Making a new blank window so that we can place all four webcam window on it
 
    smaller_image = cv.resize(frame, (0,0), fx=0.5, fy=0.5)   #Making the cam window half from width and half from height
  
    image[:height//2, :width//2] = smaller_image  #Placing them accordingly to fit in the output window
    image[height//2:, :width//2] = smaller_image
    image[:height//2, width//2:] = smaller_image
    image[height//2:, width//2:] = smaller_image 
   

    cv.imshow('frame', image)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
