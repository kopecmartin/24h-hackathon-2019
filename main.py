#!/usr/bin/env python3
"""
File: main.py
Authors:    Martin Kopec <xkopec42@gmail.com>
            Martin Krajnak <krajnakmatto@gmail.com>
            Patrik Segedy <patriksegedy@gmail.com>
            Tibor Dudlak <tibor.dudlak@gmail.com>
"""

import argparse
import os
import random
import requests

from video import Video

# arg keys
PRODUCT = "product"
EFFECT = "effect"
BACKGROUND = "background"
TEXT = "text"
ANIMATION = "animation"
FONT = "font"
STICKER = "sticker"
PLATFORM = "platform"

# used for csv data
PRODUCT_NAME = 1
PRODUCT_IMAGE = 3
PRODUCT_PRICE = 4
PRODUCT_IMAGES = 10
PRODUCT_SIZES = -1


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--background",
        default="data/videos/4KRGBcolors.mp4",
        required=False,
        help="Background",
    )
    parser.add_argument(
        "-a",
        "--animation",
        default=None,
        required=False,
        help="Animation",
    )
    parser.add_argument(
        "-f",
        "--font",
        default=None,
        required=False,
        help="Font to use",
    )
    parser.add_argument(
        "-e",
        "--effect",
        default="green",
        required=False,
        help="Color effect to use",
    )

    return parser.parse_args()


def get_random_line(csvfile="data/feeds/Footshop feed.csv"):
    lines = []
    with open(csvfile) as f:
        lines = [line for line in f]
        filesize = len(lines)

    offset = random.randrange(2, filesize)  # first 2 lines are comments

    return lines[offset]


def get_image(url):
    r = requests.get(url)
    img_name = url.split("=")[-1]+".png"
    # import ipdb; ipdb.set_trace()
    with open(img_name, "wb") as f:
        f.write(r.content)
    return img_name


if __name__ == "__main__":
    args = vars(parse_args())
    print("Hello world!\n")
    for key in args.keys():
        print(key, ":", args[key])

    data = get_random_line().split("\t")
    for item in data:
        print(item)


    downloaded = []
    images = data[PRODUCT_IMAGES].split(",") + \
        [data[PRODUCT_IMAGE].strip('"')]
    for image in images:
        # import ipdb; ipdb.set_trace()
        downloaded += [get_image(image.strip('"'))]

    print("=======================")
    print(data[PRODUCT_NAME])
    print(data[PRODUCT_PRICE])
    print(data[PRODUCT_SIZES])
    # if len(data[PRODUCT_NAME]) > 15:
    #     data[PRODUCT_NAME].
    # text = data[PRODUCT_NAME] + "\n" + data[PRODUCT_PRICE] + \
    #     "\n" + data[PRODUCT_SIZES].replace(":", "\n").replace(",", "\n").replace("é", "e")
    title = data[PRODUCT_NAME].replace('"', "")

    print("Downloda")
    print(downloaded)
    print(args)
    print(title)
    ad = Video(
        video_file=args[BACKGROUND],
        image_paths=downloaded,
        title=title,
        text=data[PRODUCT_PRICE].strip('"'),
        text_speed=60,
        font=args[FONT],
        color_effect=args[EFFECT]
    )

    # ad = Video()
    ad.play()
    for tmp_image in downloaded:
        os.remove(tmp_image)
