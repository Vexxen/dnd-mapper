#FramedWindow.py
#manages a "boxed" window, primarily adds 1 to x & y
'''   Methods
        init        newwin, box, new_panel
        redraw  (update_panels, doupdate)
        write   (addstr given string, x & y)
        plot    (addch given x, y, ch, and attributes)
'''
import curses
import curses.panel

class FramedWindow():
    def __init__(self, h, w, starty, startx):
        self.height=h
        self.width=w
        self.y=starty+1
        self.x=startx+1
        # print("FramedWindow constructor")
        self.window=curses.newwin(self.height,self.width,self.y,self.x)
        self.window.box(0,0)
        self.panel=curses.panel.new_panel(self.window)

    def redraw(self):
        curses.panel.update_panels()
        curses.doupdate()
        
    def write(self, addstrGiven, y, x):
        self.window.addstr(y+1,x+1,addstrGiven)

    def plot(self, x, y, addchGiven, attr):
        self.window.addch(y+1,x+1,addchGiven,attr)