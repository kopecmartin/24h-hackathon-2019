#!/usr/bin/env python3
"""
File: main.py
Authors:    Martin Kopec <xkopec42@gmail.com>
            Martin Krajnak <krajnakmatto@gmail.com>
            Patrik Segedy <patriksegedy@gmail.com>
            Tibor Dudlak <tibor.dudlak@gmail.com>
"""

import argparse

PRODUCT = "-p"
BACKGROUND = "-b"
TEXT = "-t"
ANIMATION = "-a"
FONT = "-f"
STICKER = "-s"
PLATFORM = "-P"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        PRODUCT,
        "--product",
        default=["data/pictures/02.jpeg"],
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
        default="Hello World!",
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
        default="data/fonts/",
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


if __name__ == "__main__":
    args = vars(parse_args())
    print("Hello world!\n")
    for key in args.keys():
        print(key, ":", args[key])
