#!/usr/bin/env python3
"""
File: main.py
Authors: Martin Kopec <xkopec42@gmail.com>
         Martin Krajnak <krajnakmatto@gmail.com>
         Patrik Segedy <>
         Tibor Dudlak <>
"""

import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tbd", required=True,
                        help="TBD")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print("Hello world!")