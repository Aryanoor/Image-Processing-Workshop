
# Image Processing Assignment using OpenCV

## Objective
The objective of this assignment is to introduce students to basic image processing techniques using **Python** and **OpenCV**. By completing the tasks, students will gain hands-on experience with image manipulation, enhancement, filtering, and transformation.

---

## Prerequisites
- **Python** installed (>= 3.6)
- **OpenCV** library (cv2) installed
- Basic understanding of image processing concepts and Python programming.

Install OpenCV using pip if not already installed:
```bash
pip install opencv-python
```

---

## Tasks
Below are the tasks that need to be implemented as part of the assignment. Each task should use appropriate OpenCV functions and be well-documented with comments.

### 1. Adding Noise to an Image
- Implement **Gaussian noise** or **Salt and Pepper noise** to an image.
- Visualize the noisy image alongside the original image.

### 2. Edge Detection Using Sobel Operator
- Perform **edge detection** using the Sobel operator.
- Extract both horizontal and vertical edges.
- Display the output images.

### 3. Histogram Equalization
- Implement histogram equalization to improve the contrast of an image.
- Compare the histogram before and after equalization.

### 4. Histogram Stretching
- Apply histogram stretching to enhance the dynamic range of the image.
- Display the transformed image and histogram.

### 5. Blurring Using Gaussian Filter
- Apply a **Gaussian blur** to an image.
- Experiment with different kernel sizes (e.g., 3x3, 5x5, 7x7).

### 6. Image Thresholding
- Implement **binary thresholding** and **adaptive thresholding**.
- Visualize the effects on grayscale images.

### 7. Image Smoothing
- Apply image smoothing techniques such as **mean filtering**.
- Compare the results with the original image.

### 8. Morphological Operations
- Perform morphological operations such as:
  - **Erosion**
  - **Dilation**
  - **Opening**
  - **Closing**
- Use a binary image for demonstration.

### 9. Contours and Object Detection
- Detect **contours** in an image and draw them on the original image.
- Count the number of detected objects (e.g., using thresholding).

### 10. Image Transformation: Rotation and Scaling
- Implement image **rotation** and **scaling** using OpenCV functions.
- Allow the user to specify the rotation angle and scaling factor.

---

## Instructions
1. **Input Image**: Use any grayscale or color image of your choice for each task.
2. **Code Organization**: Write the Python code for each task in a separate function.
3. **Visualization**: Display the input and output images using `cv2.imshow` or matplotlib.
4. **Documentation**: Add comments and explanations for each function.
5. **Submission**:
   - Submit your code in a single `.py` file.
   - Ensure that the file runs without errors.
   - Include a report (PDF or DOC) explaining each task with results (input/output images).

---

## Expected Output
- For each task, the program should display:
  - Input image
  - Processed output image
- Screenshots of all results must be included in the final report.

---

## Example Structure
Below is an example of how the code structure can look:

```python
import cv2
import numpy as np

def add_noise(image):
    # Function to add Gaussian noise
    pass

def sobel_edge_detection(image):
    # Function to apply Sobel operator
    pass

def histogram_equalization(image):
    # Function to perform histogram equalization
    pass

def main():
    image = cv2.imread('input.jpg', 0)  # Read image in grayscale

    # Task 1: Adding Noise
    noisy_image = add_noise(image)
    cv2.imshow('Noisy Image', noisy_image)

    # Task 2: Sobel Edge Detection
    sobel_edges = sobel_edge_detection(image)
    cv2.imshow('Sobel Edges', sobel_edges)

    # Add other functions here...

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

---

## Evaluation Criteria
1. Correctness of code implementation for each task.
2. Proper organization and modularity of code.
3. Output image quality and visualization.
4. Report clarity and explanation.


---

## References
- [OpenCV Documentation](https://docs.opencv.org/)
- [Python Programming](https://www.python.org/)

---

Good luck and happy coding!

---
