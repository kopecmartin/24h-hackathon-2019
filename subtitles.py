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
        self.pos = 0

    def step(self):
        if self.counter == self.speed:
            self.index = 0 if self.index >= self.length-1 else self.index + 1
            self.counter = 0
        self.counter += 1

    def get_size(self):
        return cv2.getTextSize(
            self.lines[self.index], self.font, self.font_scale, self.thick
            )[0]

    def render(self, frame, width, height):
        cv2.putText(
            frame, self.lines[self.index],
            (width, height),
            self.font,
            self.font_scale,
            (255, 255, 255),
            self.thick,
            cv2.LINE_AA
            )

    def show_centered(self, frame, width, height):
        size = self.get_size()
        self.render(
            frame,
            int(width/2) - int(size[0]/2),
            int(height/2) - int(size[1]/2)
            )
        self.step()

    def show_low(self, frame, width, height):
        size = self.get_size()
        self.render(
            frame,
            int(width/2) - int(size[0]/2),
            height - int(size[1]*2)
            )
        self.step()

    def show_continous(self, frame, width, height):
        size = self.get_size()
        self.render(
            frame,
            self.pos,
            height - int(size[1]*3)
            )
        self.step()
        self.pos = 0 if self.pos + self.get_size()[0] >= width else self.pos + 6
