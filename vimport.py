#!/usr/bin/python3
from PIL import Image, ImageSequence
import numpy as np
import pyautogui
import random
import time

def compose(x, y):
    # Config values
    file = 'example.gif'  # Change this to your GIF name
    xstart = 119  # X coord of the farthest right point inside the leftmost note
    xincrement = 122  # Pixel count between notes
    xmax = xstart + xincrement * 13  # Max note coord, likely no need to change
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

    img = Image.open(file)  # Change this to your GIF file
    frames = np.array([np.array(frame.copy().convert('RGB').getdata(), dtype=np.uint8).reshape(frame.size[1], frame.size[0], 3) for
         frame in ImageSequence.Iterator(img)]).transpose(1, 2, 0, 3)
    frames = np.flip(frames, 0)
    pixel = frames[y][x]  # Generate an array from GIF, extract RGB data for a single pixel

    x = xstart + xincrement * 4
    pyautogui.moveTo(accidentalbutton_x, accidentalbutton_y)
    pyautogui.click()
    print("click {0}, {1}".format(str(accidentalbutton_x), str(accidentalbutton_y)))
    time.sleep(random.uniform(0.1, 0.2))

    for i in range(512):
        print("processing frame {0}".format(str(i)))
        if i == 498:
            pyautogui.moveTo(nextbutton_x, nextbutton_y)
            pyautogui.click()
            print("click {0}, {1}".format(str(nextbutton_x), str(nextbutton_y)))
            x = xstart
            time.sleep(random.uniform(0.1, 0.2))
        if pixel[i][0] == color_white:
            y = y0
        elif pixel[i][0] == color_black:
            y = y2
        else:
            y = y1
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print("click {0}, {1}".format(str(x), str(y)))
        time.sleep(random.uniform(0.02, 0.03))
        if x >= xmax:
            if i == 511:
                pyautogui.moveTo(exitbutton_x, exitbutton_y)
                pyautogui.click()
                print("click {0}, {1}".format(str(exitbutton_x), str(exitbutton_y)))
                time.sleep(random.uniform(0.5, 0.7))
                pyautogui.moveTo(confirmbutton_x, confirmbutton_y)
                pyautogui.click()
                print("click {0}, {1}".format(str(confirmbutton_x), str(confirmbutton_y)))
                time.sleep(random.uniform(0.7, 0.9))
                pyautogui.moveTo(successbutton_x, successbutton_y)
                pyautogui.click()
                print("click {0}, {1}".format(str(successbutton_x), str(successbutton_y)))
            else:
                pyautogui.moveTo(nextbutton_x, nextbutton_y)
                pyautogui.click()
                print("click {0}, {1}".format(str(nextbutton_x), str(nextbutton_y)))
                x = xstart
                time.sleep(random.uniform(0.1, 0.2))
        else:
            x += xincrement


if __name__ == '__main__':
    coords = input("coordinate (x y): ").split()
    compose(int(coords[0]), int(coords[1]))