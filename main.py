#!/usr/bin/env python3
"""
File: main.py
Authors:    Martin Kopec <xkopec42@gmail.com>
            Martin Krajnak <krajnakmatto@gmail.com>
            Patrik Segedy <patriksegedy@gmail.com>
            Tibor Dudlak <tibor.dudlak@gmail.com>
"""

import argparse
import random

# used for argparse
PRODUCT = "-p"
BACKGROUND = "-b"
TEXT = "-t"
ANIMATION = "-a"
FONT = "-f"
STICKER = "-s"
PLATFORM = "-P"

# used for csv data
PRODUCT_NAME = 1
PRODUCT_IMAGE = 3
PRODUCT_PRICE = 4
PRODUCT_IMAGES = 10
PRODUCT_SIZES = -1



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        PRODUCT,
        "--product",
        default=None,
        help="Product images",
    )
    parser.add_argument(
        BACKGROUND,
        "--background",
        default="data/videos/4KRGBcolors.mp4",
        required=False,
        help="Background",
    )
    parser.add_argument(
        TEXT,
        "--text",
        default=None,
        required=False,
        help="Text to display",
    )
    parser.add_argument(
        ANIMATION,
        "--animation",
        default=None,
        required=False,
        help="Animation",
    )
    parser.add_argument(
        FONT,
        "--font",
        default=None,
        required=False,
        help="Font to use",
    )
    parser.add_argument(
        STICKER,
        "--sticker",
        default="data/stickers/doge.png",
        required=False,
        help="Font to use",
    )
    parser.add_argument(
        PLATFORM,
        "--platform",
        default=None,
        required=False,
        help="Target platform",
    )

    return parser.parse_args()


def get_random_line(csvfile="data/feeds/Footshop feed.csv"):
    lines = []
    with open(csvfile) as f:
        lines = [line for line in f]
        filesize = len(lines)

    offset = random.randrange(2, filesize)  # first 2 lines are comments

    return lines[offset]


if __name__ == "__main__":
    args = vars(parse_args())
    print("Hello world!\n")
    for key in args.keys():
        print(key, ":", args[key])

    data = get_random_line().split("\t")
    for item in data:
        print(item)

    print("-----")

    print(data[PRODUCT_IMAGE])
    print(data[PRODUCT_IMAGES].split(","))

    print(data[PRODUCT_NAME])
    print(data[PRODUCT_PRICE])
    print(data[PRODUCT_SIZES])
