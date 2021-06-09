import cv2
import numpy as np
import time

# To save the output in a file output.avi

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = cv2.VideoWriter("output.png", fourcc, 20.0, (640, 480))

# Starting the webcamera

capture = cv2.VideoCapture(0)

# Allowing the webcam to start by making the code sleep for 2 seconds
time.sleep(2)

bg = 0

for i in range(0, 60):
    ret, bg = capture.read()

# Flipping the background
bg = np.flip(bg, axis=1)

# Reading the captured frame until the camera is open

while(capture.isOpened()):
    ret, img = capture.read()
    if not ret:
        break
    # Flipping the image for consistency
    img = np.flip(img, axis=1)

    # Converting the color from RGB to HSV
    # using Bger color value....

    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
