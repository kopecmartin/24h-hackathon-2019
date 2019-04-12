#!/usr/bin/env python3
"""
File: main.py
Authors:    Martin Kopec <xkopec42@gmail.com>
            Martin Krajnak <krajnakmatto@gmail.com>
            Patrik Segedy <patriksegedy@gmail.com>
            Tibor Dudlak <tibor.dudlak@gmail.com>
"""

import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--products", required=True,
                        help="Product images")
    parser.add_argument("-b", "--background", required=True,
                        help="Background")
    parser.add_argument("-t", "--text", required=True,
                        help="Text to display")

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print("Hello world!")
    for arg in args:
        print(arg)
