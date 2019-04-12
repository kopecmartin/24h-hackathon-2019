import cv2

from shape import Shape
from subtitles import Subtitles
from effect import Effect


class Video:
    def __init__(self,
                 video_file="./data/videos/Pexels Videos 5004.mp4",
                 width=1920,
                 height=1080,
                 FPS=60,
                 text="FAST\nFURIOUS\nFANCY",
                 title="Topanka",
                 image_paths=[
                     "data/pictures/topanka.png",
                     "data/pictures/topanka.png"
                 ],
                 text_speed=20,
                 font=None,
                 speed=6,
                 color_effect="red",
                 animation=None):
        self.video_file = video_file
        self.width = width
        self.height = height
        self.FPS = FPS
        self.text = text
        self.title = title
        self.image_paths = image_paths
        self.text_speed = text_speed
        self.font = font
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
        index = 0

        # find out the video dimensions
        self.width, self.height, _ = cap.read()[1].shape

        shape = Shape(
            self.width,
            self.height,
            self.paint_x,
            self.paint_y,
            self.speed,
            self.image_paths[index % len(self.image_paths)],
            'curve2',
        )

        effect = Effect(self.color_effect)
        text = Subtitles(self.text, self.text_speed, acceleration=4)
        # text = Subtitles('FAST\nFURIOUS\nFANCY', self.text_speed, './data/fonts/Dogfish/Dogfish.ttf')

        title = Subtitles(self.title, self.text_speed, font=self.font)
        title.font_scale = 1
        title.thick = 2
        # Read until video is completed
        while cap.isOpened():
            # Capture frame-by-frame
            ret, frame = cap.read()
            try:
                self.width = frame.shape[1]
                self.height = frame.shape[0]
            except AttributeError:
                break
            # import ipdb; ipdb.set_trace()
            if ret is True:
                shape.paint(frame)
                frame = effect.apply(frame)
                frame = title.show_title(frame, self.width, self.height)
                # frame = text.show_low(frame, self.width, self.height)
                frame = text.show_price(frame, self.width, self.height)
                # if title.counter == 1:
                #     text.counter = title.counter
                cv2.imshow("Frame", frame)
                # print(self.image_paths[index % len(self.image_paths)], index + 1)
                if shape.end:
                    index += 1
                    if index >= len(self.image_paths):
                        index = 0

                    shape = Shape(
                        self.width,
                        self.height,
                        self.paint_x,
                        self.paint_y,
                        self.speed,
                        self.image_paths[index % len(self.image_paths)],
                        'curve2',
                    )

                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    return
            # Break the loop
            else:
                break

        # When everything done, release the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()
