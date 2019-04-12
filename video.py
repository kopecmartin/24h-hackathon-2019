import cv2

from shape import Shape
from subtitles import Subtitles
from effect import Effect


class Video:
    def __init__(self,
                 video_file="Pexels Videos 5004.mp4",
                 width=1920,
                 height=1080,
                 FPS=60,
                 text="FAST\nFURIOUS\nFANCY",
                 image="data/pictures/topanka.png",
                 text_speed=20,
                 speed=6,
                 color_effect="red",
                 animation=None):
        self.video_file = video_file
        self.width = width
        self.height = height
        self.FPS = FPS
        self.text = text
        self.image = image
        self.text_speed = text_speed
        self.speed = speed
        self.color_effect = color_effect
        self.animation = animation
        self.seconds = 10
        self.radius = 150

        self.paint_x = 0
        self.paint_y = 0

    def play(self):
        # Create a VideoCapture object and read from input file
        # If the input is the camera, pass 0 instead of the video file name
        cap = cv2.VideoCapture(self.video_file)

        # Check if camera opened successfully
        if cap.isOpened() is False:
            print("Error opening video stream or file")

        shape = Shape(
            self.radius,
            None,
            self.paint_x,
            self.paint_y,
            self.speed,
            (0, 0, 0),
            self.image,
            0,
        )

        effect = Effect(self.effect)
        text = Subtitles(self.text, self.text_speed)
        # text = Subtitles('FAST\nFURIOUS\nFANCY', self.text_speed, './data/fonts/Dogfish/Dogfish.ttf')
        # text = Subtitles('FAST\nFURIOUS\nFANCY', self.text_speed, './data/fonts/Dogfish/Dogfish Oblique.ttf')
        # Read until video is completed
        while cap.isOpened():
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret is True:
                shape.paint(frame, self.width, self.height)
                frame = effect.apply(frame)
                frame = text.show_continous(frame, self.width, self.height)
                frame = text.show_low(frame, self.width, self.height)
                frame = text.show_centered(frame, self.width, self.height)
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
