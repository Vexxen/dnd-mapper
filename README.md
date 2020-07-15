# dnd-mapper
A D&amp;D mapping tool based on a Shell Scripting class project using the Curses library.  The map you create will be saved as a text file for conversion into a graphical map using ImageMagick.

## Running
./painter.py <textfile>
ex: ./painter.py caverns_deep.txt
if the text file is empty, or does not exist, the painter will create one with dimensions at the size of the terminal.

## Navigation
Similar to vim
#### Movement Commands:
j - move down  
k - move up  
l - move right  
h - move left  

shift + <movement command> - Paint current cell, then move in selected direction

#### other commands:
w or s - open save window (type a name then hit Enter to save)
Q - Quit out of window


## Files

#### painter.py
The Driver file.  Simply calls PainterWindow.py in a curses.wrapper.

#### Cell.py
Instantiates the Cell class.  Each cell consists of 2 characters in order to create a square character representation in the terminal window.

#### FramedWindow.py
Instantiates the FramedWindow class.  Each FramedWindow is a slightly modified curses.window for displaying on the screen

#### PainterWindow.py
Instantiates the PainterWindow Class.  This is the main backbone of the script.  PainterWindow.py will create the mainpane, statuspane, and save_window.  Contains the main program loop for generating each D&D map.
