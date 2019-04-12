import cv2
import numpy as np

class Shape:
    """docstring for Shape"""
    def __init__(self, size, shape, x, y, speed, color, image, animation):
        self.size = size
        self.shape = shape
        self.x = x
        self.y = y
        self.color = color
        self.image = image
        self.animation = animation
        self.speed = speed

    def paint(self, frame, frame_width):
        self._next_pos(frame_width)
        if self.shape == 'circle':
            cv2.circle(frame, (self.x, self.y), self.size, self.color, -1)

    def _next_pos(self, frame_width):
        if self.animation == 0:
            self.x += self.speed
            if self.x > frame_width:
                self.x = 0
