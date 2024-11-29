import cv2
import numpy as np 
import matplotlib.pyplot as plt 

# Function to hide an image inside another image using LSB encoding
def hide_image_inside_another_image(cover_image, hidden_image, wants_save_image=1):
    # Resize hidden image to match the cover image dimensions
    hidden_image = cv2.resize(hidden_image, cover_image.shape[::-1])

    # Clear the least significant bit (LSB) of the cover image
    cover_image = cover_image & 0b11111110

    # Shift the hidden image to the LSB
    hidden_image = hidden_image >> 7

    # Combine both images using bitwise OR
    final_image = cover_image | hidden_image

    if wants_save_image:
        cv2.imwrite('final_image.png', final_image)  # Save the stego image in a lossless format

    return final_image

# Function to extract the hidden image from the stego image
def extract_hidden_image(image, wants_save_image=1):
    # Extract the least significant bit from the image
    hidden_image = image & 0b00000001

    # Scale back to the 0-255 range for visualization
    hidden_image = hidden_image * 255

    if wants_save_image:
        cv2.imwrite('extracted_hidden_image.png', hidden_image)  # Save the extracted hidden image

    return hidden_image

# Paths to the cover and hidden images
cover_image_path = 'img/Tehran.jpg' 
hidden_image_path = 'img/WW0.jpg' 

# Load the images (grayscale)
cover_image = cv2.imread(cover_image_path, cv2.IMREAD_GRAYSCALE)
hidden_image = cv2.imread(hidden_image_path, cv2.IMREAD_GRAYSCALE)

# Step 1: Embed the hidden image into the cover image
stego_image = hide_image_inside_another_image(cover_image, hidden_image, wants_save_image=1)

# Step 2: Extract the hidden image from the stego image
extracted_image = extract_hidden_image(stego_image)

# Step 3: Display the images using Matplotlib
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(cover_image, cmap='gray')
axes[0].set_title("Cover Image")
axes[1].imshow(stego_image, cmap='gray')
axes[1].set_title("Stego Image (With Hidden Image)")
axes[2].imshow(extracted_image, cmap='gray')
axes[2].set_title("Extracted Hidden Image")

plt.show()
