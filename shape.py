import cv2


class Shape:
    """docstring for Shape"""

    def __init__(self, size, shape, x, y, speed, color, image, animation):
        self.end = False
        self.size = size
        self.shape = shape
        self.x = x
        self.y = y
        self.color = color
        self.image = cv2.imread(image, -1) if image else None
        height, width, depth = self.image.shape
        imgScale = 600/width
        newX, newY = self.image.shape[1]*imgScale, self.image.shape[0]*imgScale
        self.image = cv2.resize(self.image, (int(newX), int(newY)))
        # self.image = cv2.resize(self.image, (int(250), int(200)))
        self.imagegrey = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.animation = animation
        self.speed = speed
        # rows, cols, channels
        self.dim = self.image.shape

    def paint(self, frame, frame_width, frame_height):
        self._next_pos(frame_width, frame_height)
        roi = frame[0 : self.dim[0], 0 : self.dim[1]] # noqa: 203
        __, mask = cv2.threshold(self.imagegrey, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        # Now black-out the area of logo in ROI
        frame_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
        # Take only region of logo from logo image.
        image_fg = cv2.bitwise_and(self.image, self.image, mask=mask)
        # Put logo in ROI and modify the main image
        dst = cv2.add(frame_bg, image_fg)

        if self.image is not None:
            frame[
                self.x : (self.dim[0] + self.x),  # noqa: 203
                self.y : (self.dim[1] + self.y),  # noqa: 203
            ] = dst
        elif self.shape == "circle":
            cv2.circle(frame, (self.x, self.y), self.size, self.color, -1)

    def _next_pos(self, frame_width, frame_height):
        if self.animation == 0:
            self.x += self.speed
            self.y += self.speed
            if self.x + self.dim[0] > frame_height:
                self.x = 0
            if self.y > frame_width - self.dim[1]:
                self.y = 0
                self.end = True
