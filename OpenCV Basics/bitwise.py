import cv2
import numpy as np  

# Create a blank black image of size 400x400
blank = np.zeros((400, 400), dtype='uint8')

# Draw a filled white rectangle on the blank image
rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

# Draw a filled white circle on the blank image
circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)

# Display the rectangle and circle
cv2.imshow('Rectangle', rectangle)
cv2.imshow('Circle', circle)

# Perform bitwise AND operation: keeps only the intersecting regions of the rectangle and circle
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('Bitwise AND', bitwise_and)

# Perform bitwise OR operation: combines the non-intersecting and intersecting regions of the rectangle and circle
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('Bitwise OR', bitwise_or)

# Perform bitwise XOR operation: keeps only the non-intersecting regions of the rectangle and circle
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('Bitwise XOR', bitwise_xor)

# Perform bitwise NOT operation: inverts the bits of the circle
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow('Circle NOT', bitwise_not)

# Wait until a key is pressed before closing all windows
cv2.waitKey(0)
