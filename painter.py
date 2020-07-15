#!/usr/bin/env python3
#driver program, approx 10 lines, curses.wrapper
# from curses import wrapper
import sys
import curses
from PainterWindow import PainterWindow
from FramedWindow import FramedWindow
from Cell import Cell

# import curses.panel

def main(stdscr):
    # myFile='dungeon.txt'

    # fo=open(myFile,"w")
    # (y, x) = curses.getmaxyx()
    # y-=5
    # x-=1
    stdscr.clear()
    curses.curs_set(False)

    # main_painter_window = FramedWindow(curses.LINES-5, curses.COLS-1, 0, 0)
    # # main_painter_window = FramedWindow(y, x, 0, 0)
    # main_painter_window.redraw()
    # # myCell = Cell(2,2,'#',main_painter_window)
    # # myCell.draw()
    # # secondCell = Cell(2,3,'.',main_painter_window)
    # # secondCell.draw()

    

    # status_window = FramedWindow(3, curses.COLS-1, curses.LINES-5, 0)
    # status_window.write("Status Bar",0,5)
    # status_window.redraw()

    # myPainter=PainterWindow("testFile.txt", main_painter_window, stdscr)
    # main_painter_window.redraw()
    # # (statY,statX)=status_window.getbegyx()
    # stdscr.refresh()#must call refresh to update text changes on screen
    # stdscr.getkey()
    # try:
    if len(sys.argv) != 2:
        raise Exception("Usage: ./painter.py <filename>")
    else:
        myPainter=PainterWindow(sys.argv[1], stdscr)
        myPainter.run()
    # except Exception as e:
    #     print(e)
    #     exit(1)

# wrapper(main)

if __name__=="__main__":
    curses.wrapper(main)