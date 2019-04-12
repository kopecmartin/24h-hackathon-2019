import cv2
import numpy as np
from shape import Shape

width = 1800
height = 1080
FPS = 24
seconds = 10
radius = 150

paint_x = 0
paint_y = 0
speed = 6

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture("Pexels Videos 5004.mp4")

# Check if camera opened successfully
if cap.isOpened() is False:
    print("Error opening video stream or file")

shape = Shape(
    radius,
    None,
    paint_x,
    paint_y,
    speed,
    (0, 0, 0),
    "data/pictures/topanka.png",
    0,
)
# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret is True:
        shape.paint(frame, width, height)

        cv2.imshow("Frame", frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
