import cv2
import numpy as np 
from consts import path  # Import image path

# Load the image to be transformed
img = cv2.imread(path)
cv2.imshow('Original', img)

# Function to rotate an image by a specified angle
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]  # Get the image dimensions

    # If no rotation point is specified, use the center of the image
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # Get the rotation matrix
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    
    # Apply the rotation transformation
    return cv2.warpAffine(img, rotMat, (width, height))

# Rotate the image by -45 degrees and display the result
rotated = rotate(img, -45)
cv2.imshow('Rotated', rotated)

# Rotate the image by -90 degrees and display the result
rotated_rotated = rotate(img, -90)
cv2.imshow('Rotated Rotated', rotated_rotated)

# Flip the image both horizontally and vertically
flip = cv2.flip(img, -1)
cv2.imshow('Flip', flip)

# Wait until a key is pressed before closing all windows
cv2.waitKey(0)
