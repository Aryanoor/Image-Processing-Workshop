import cv2 
import numpy as np  
from consts import path  # Import the path of the image to be loaded

# Read the image from the specified path
img = cv2.imread(path)

# Split the image into Blue, Green, and Red channels
B, G, R = cv2.split(img)
print(B)  # Print the Blue channel to the console

# Modify Blue and Green channels
B = np.zeros_like(B)  # Set all pixels in Blue channel to 0 (black)
G = 255 * np.ones_like(G)  # Set all pixels in Green channel to 255 (green)

# Display individual channels
cv2.imshow("Blue Channel", B)
cv2.imshow("Green Channel", G)
cv2.imshow("Red Channel", R)

# Merge the modified channels back into a single image
merged_img = cv2.merge([B, G, R])
cv2.imshow("Merged", merged_img)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Apply Gaussian blur to the image
blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

# Apply Canny edge detection to the blurred image
canny = cv2.Canny(blur, 130, 200)
cv2.imshow('Canny Edges', canny)

# Dilate the edges to make them thicker
dilated = cv2.dilate(canny, kernel=(1, 1), iterations=3)
cv2.imshow('Dilated', dilated)

# Resize the image to 500x500 pixels using cubic interpolation
resized = cv2.resize(dilated, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

# Crop a region of interest from the image
cropped = img[154:602, 335:802]
cv2.imshow('Cropped', cropped)

# Apply blur, Canny edge detection, and dilation to the cropped image
cropped_blur = cv2.GaussianBlur(cropped, (5, 5), cv2.BORDER_DEFAULT)
canny = cv2.Canny(cropped_blur, 130, 200)
dilated = cv2.dilate(canny, (3, 3), iterations=3)
cv2.imshow('Dilated', dilated)

# Wait until a key is pressed before closing all windows
cv2.waitKey(0)
