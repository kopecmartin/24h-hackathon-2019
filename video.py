import cv2
import numpy as np

width = 1280
height = 720
FPS = 24
seconds = 10
radius = 150

paint_h = 800
paint_x = 0
speed = 6

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('Pexels Videos 5004.mp4')

# Check if camera opened successfully
if (cap.isOpened() is False):
    print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret is True:
        # Display the resulting frame
        cv2.circle(frame, (paint_x, paint_h), radius, (0, 0, 0), -1)
        cv2.imshow('Frame', frame)

        paint_x += speed
        # paint_h += speed
        if paint_x > width:
            paint_x = 0

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
