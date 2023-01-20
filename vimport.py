#!/usr/bin/env python3
from PIL import Image, ImageSequence
import numpy as np
import pyautogui
import random
import time

def click(x, y):
    pyautogui.click(x, y)
    print("click {0}, {1}".format(str(x), str(y)))

def drag(x0, x1, y):
    pyautogui.click(x0, y)
    time.sleep(random.uniform(0.02, 0.04))
    pyautogui.dragTo(x1, y, random.uniform(0.1, 0.2), pyautogui.easeOutQuad, button='left')

def compose(x, y):
    # Config values
    file = 'example.gif'  # Path to GIF
    xstart = 119  # X coord of the farthest right point inside the leftmost note
    xstep = 122  # Pixel count between notes
    xmax = xstart + xstep * 13  # Max note coord, likely no need to change
    y0 = 369  # Y coord for low B
    y1 = 536  # Y coord for low B
    y2 = 600  # Y coord for high F
    color_white = 255  # Red value for white, get this from vconv.py
    color_black = 8  # Red value for black, get this from vconv.py
    nextbutton_x = 1615  # X and Y coords for the next screen arrow
    nextbutton_y = 662
    accidentalbutton_x = 1250  # X and Y coords for the accidental button
    accidentalbutton_y = 100
    exitbutton_x = 1646
    exitbutton_y = 777
    confirmbutton_x = 624  # X and Y coords for the checkbox on the save confirmation dialog
    confirmbutton_y = 681
    successbutton_x = 912  # X and Y coords for the checkbox on the save successful dialog
    successbutton_y = 687

    # Generate an array from GIF, extract RGB data for a single pixel
    img = Image.open(file)
    frames = np.array([np.array(frame.copy().convert('RGB').getdata(), dtype=np.uint8).reshape(frame.size[1], frame.size[0], 3) for
         frame in ImageSequence.Iterator(img)]).transpose(1, 2, 0, 3)
    frames = np.flip(frames, 0)
    pixel = frames[y][x]

    x = xstart + xstep * 4   # Initialize vars
    xdrag = x

    click(accidentalbutton_x, accidentalbutton_y)
    time.sleep(random.uniform(0.05, 0.1))
    click(accidentalbutton_x, accidentalbutton_y)
    time.sleep(random.uniform(0.075, 0.15))

    for i in range(512):
        print("processing frame {0}".format(str(i)))

        if i == 498:  # Workaround for end
            if xdrag < x - xstep:
                drag(xdrag, x - xstep, y)
            else:
                pg.click(xdrag, y)
                time.sleep(random.uniform(0.02, 0.05))
            click(nextbutton_x, nextbutton_y)
            x = xstart
            xdrag = xstart
            time.sleep(random.uniform(0.075, 0.15))

        if pixel[i][0] == color_white:  # Set Y value
            ynext = y0
        elif pixel[i][0] == color_black:
            ynext = y2
        else:
            ynext = y1
        if i == 0:
            y = ynext

        if y != ynext:  # Input note
            if xdrag == x - xstep:
                click(xdrag, y)
            elif x != xstart:
                drag(xdrag, x - xstep, y)
            time.sleep(random.uniform(0.02, 0.05))
            xdrag = x
            y = ynext

        if x >= xmax:
            if i == 511:  # Input last note, save, and exit
                if xdrag < x:
                    drag(xdrag, x, y)
                else:
                    click(xdrag, y)
                time.sleep(random.uniform(0.02, 0.05))
                click(exitbutton_x, exitbutton_y)
                time.sleep(random.uniform(0.5, 0.7))
                click(confirmbutton_x, confirmbutton_y)
                time.sleep(random.uniform(0.8, 1))
                click(successbutton_x, successbutton_y)

            else:  # Input note and click next button
                if xdrag < x:
                    drag(xdrag, x, y)
                else:
                    click(xdrag, y)
                time.sleep(random.uniform(0.02, 0.05))
                click(nextbutton_x, nextbutton_y)
                x = xstart
                xdrag = xstart
                time.sleep(random.uniform(0.075, 0.15))
        else:
            x += xstep


if __name__ == '__main__':
    coords = input("coordinate (x y): ").split()
    compose(int(coords[0]), int(coords[1]))