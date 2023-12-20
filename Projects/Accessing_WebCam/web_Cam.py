import cv2 as cv
import numpy as np

#accessing the laptop camera
cap = cv.VideoCapature(0)  #by putting 0 here it will access the primary camera or the webcam of laptop
                           #if we need to access external camera we need to specify by writing 1,2,3,... and so on.

while True:
  ret, frame = cap.read()  #cap.read() will read the frames per millisecond of the captured video.
                           #ret will return the frames.
  cv.imshow(frame)         #this will show the frames captured by the webcam.
  if cv.waitKey(1) == ord('27'):    #cv.waitKey(1) will wait for 1 Millisecond after pressing the "escape" key
    break                           #('ord' refers to ordinal value & ASCII value of escape key is 27)
cap.release()
cv.destroyAllWindows()
    
