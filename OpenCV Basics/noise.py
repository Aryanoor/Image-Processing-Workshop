import cv2
import numpy as np
import matplotlib.pyplot as plt 
from consts import path  # Import image path

# Function to add Gaussian noise to an image
def add_gaussian_noise(image, mean=0, std=25):
    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)  # Add noise to the original image
    return noisy_image

# Function to add salt-and-pepper noise to an image
def add_salt_and_pepper_noise(image, noise_ratio=0.1):
    noisy_image = image.copy()
    h, w, c = noisy_image.shape
    noisy_pixels = int(h * w * noise_ratio)
    
    for _ in range(noisy_pixels):
        row, col = np.random.randint(0, h), np.random.randint(0, w)
        if np.random.rand() < 0.5:
            noisy_image[row, col] = [0, 0, 0]  # Black pixel (salt)
        else:
            noisy_image[row, col] = [255, 255, 255]  # White pixel (pepper)
    
    return noisy_image

# Load the original image
original_image = cv2.imread(path)

# Add Gaussian and salt-and-pepper noise to the image
noisy_image_gauss = add_gaussian_noise(original_image, mean=0, std=25)
noisy_image_salt = add_salt_and_pepper_noise(original_image)

# Display the original image and the noisy images
fig, axes = plt.subplots(1, 3, figsize=(10, 20))
fig.suptitle('Image Processing Results')
axes[0].imshow(original_image)
axes[0].set_title("Original Image")
axes[0].axis('off')
axes[1].imshow(noisy_image_gauss)
axes[1].set_title("Gaussian Noise")
axes[1].axis('off')
axes[2].imshow(noisy_image_salt)
axes[2].set_title("Salt & Pepper Noise")
axes[2].axis('off')

plt.show()
