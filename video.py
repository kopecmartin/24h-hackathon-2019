import cv2
import numpy as np

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
cap = cv2.VideoCapture('Pexels Videos 5004.mp4')
image = cv2.imread('topanka.png', -1)

# Check if camera opened successfully
if (cap.isOpened() is False):
    print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret is True:
        # Display the resulting frame
        # cv2.circle(frame, (paint_x, paint_y), radius, (0, 0, 0), -1)

        # I want to put logo on top-left corner, So I create a ROI
        rows, cols, channels = image.shape
        roi = frame[0:rows, 0:cols]
        # Now create a mask of logo and create its inverse mask also
        imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(imagegray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        # Now black-out the area of logo in ROI
        frame_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
        # Take only region of logo from logo image.
        image_fg = cv2.bitwise_and(image, image, mask=mask)
        # Put logo in ROI and modify the main image
        dst = cv2.add(frame_bg, image_fg)

        paint_x += speed
        paint_y += speed
        if paint_x + cols > height:
            paint_x = 0
        if paint_y > width - cols:
            paint_y = 0
        # import ipdb; ipdb.set_trace()
        print("paint_x:" + str(cols+paint_x))
        print("paint_y:" + str(paint_y))

        frame[paint_x:rows+paint_x, paint_y:cols+paint_y] = dst
        cv2.imshow('Frame', frame)

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
