#!/usr/bin/python3
from PIL import Image, ImageSequence
import csv
import numpy as np
import os
import subprocess

# Generate sample output for debugging
subprocess.call(  # Example ffmpeg command to convert a video to a 13x10 GIF for importing
    'ffmpeg -i', 'example.mp4', '-lavfi "format=pix_fmts=gray,fps=8,scale=13:10:flags=lanczos,split [o1] [o2];[o1] palettegen=max_colors=4 [p]; [o2] fifo [o3];[o3] [p] paletteuse=new=1:dither=none"', 'example.gif')
img = Image.open('example.gif')
frames = np.array(
    [np.array(frame.copy().convert('RGB').getdata(), dtype=np.uint8).reshape(frame.size[1], frame.size[0], 3) for
     frame in ImageSequence.Iterator(img)]).transpose(1, 2, 0, 3)
frames = np.flip(frames, 0)  # Convert GIF to array of RGB values
print(frames)
try:
    os.mkdir('out')
except OSError as error:
    print(error)
for i in range(len(frames)):  # Write data out to CSV files for debugging
    for j in range(len(frames[i])):
        with open("out/" + str(j) + "_" + str(i), '+w') as data:
            csvWriter = csv.writer(data, delimiter=',')
            csvWriter.writerows(frames[i][j])