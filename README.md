Composer Island Bot
=========

Description
--------------
This repository currently includes one script, to import video files into My Singing Monsters™ as Glowbe animations.  
In the future there may be other scripts for importing songs from various sources.  
For the video script, it is highly recommended to name your Glowbes with cartesian coordinates, with 0,0 being the bottom left.  
This program is WIP and many things are currently hardcoded, it might not work on your system due to different aspect ratios.  

Installation (Tested on Arch Linux)
--------------

```git clone https://github.com/haxalicious/composer-island-bot.git
cd composer-island-bot
./setup.py
```

Usage
--------------
## Converting Video
Edit the FFmpeg command in vconv.py with your correct file names, framerate and resolution. Framerate is determined by (song BPM * 2 / 60).  
Run 
```./vconv.py```

## Importing Video
 - Edit config options in vimport.py. You need to adjust everything under "config values", X and Y coordinates can be obtained using something like GIMP from a screenshot.
 - Configuring X and Y coordinates for pixels only needs to be done once.
Open the Compose UI in-game, then run:
```./vimport.py```
Enter the coords for the Glowbe you want. The script will automate the inputs required.

Disclaimer
--------------
> My Singing Monsters™ is a registered trademark of Big Blue Bubble Inc.
> All trademarks referenced herein are the properties of their respective owners. The program is provided "AS IS", only for educational purposes, without warranty of any kind. Developer is not responsible for any loss or damage from its use, including banned accounts, lost game progress etc.