import cv2
import numpy as np 

# Create a blank black image of size 500x500
blank = np.zeros((500, 500, 3), dtype='uint8')
cv2.imshow('Blank', blank)

# 1. Paint a section of the image yellow (RGB: 0,255,255)
blank[200:300, 300:400] = 0, 255, 255
cv2.imshow('Yellow', blank)

# 2. Draw a filled green rectangle (top-left: (0,0), bottom-right: half of the image size)
cv2.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv2.imshow('Rectangle', blank)

# 3. Draw a filled red circle at the center of the image with a radius of 40 pixels
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv2.imshow('Circle', blank)

# 4. Draw a white line from point (100, 250) to (300, 400)
cv2.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=3)
cv2.imshow('Line', blank)

# 5. Write text "Hello, my name is Aryan!!!" at the specified location with white color
cv2.putText(blank, 'Hello, my name is Aryan!!!', (0, 100), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv2.imshow('Text', blank)

# Wait until a key is pressed before closing all windows
cv2.waitKey(0)
