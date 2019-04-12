import cv2


class Subtitles:
    """docstring for."""

    def __init__(self, text, speed=20, font=cv2.FONT_HERSHEY_PLAIN):
        self.lines = text.splitlines()
        self.length = len(self.lines)
        self.speed = speed
        self.index = 0
        self.counter = 0
        # heigth
        self.font_scale = 5
        # thickeness
        self.thick = 6
        self.font = font

    def show(self, frame, width, height):
        size = cv2.getTextSize(
            self.lines[self.index], self.font, self.font_scale, self.thick
            )[0]
        cv2.putText(
            frame, self.lines[self.index],
            (int(width/2) - int(size[0]/2), int(height/2) - int(size[1]/2)),
            self.font,
            self.font_scale,
            (255, 255, 255),
            self.thick,
            cv2.LINE_AA
            )

        if self.counter == self.speed:
            self.index = 0 if self.index >= self.length-1 else self.index + 1
            self.counter = 0
        self.counter += 1
