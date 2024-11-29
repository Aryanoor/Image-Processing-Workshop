import cv2
from consts import path 

# Read the image from the specified path
my_img = cv2.imread(path)

# Display the image in a window named 'Frame Name'
cv2.imshow("Frame Name", my_img)

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

RUN = True  # Flag to control the while loop

while RUN:
    # Capture a frame from the video stream
    is_true, frame = cap.read()

    if is_true:  # If the frame was successfully captured
        # Show the captured video frame in a window named 'Video'
        cv2.imshow('Video', frame)

        # If the 'q' key is pressed, exit the loop
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break  # If frame capture fails, break the loop

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
