'''
PainterWindow.py
    init - opens file, initializes the Cell Objects
    toggle_glyph - switches through the 4 possible brushes
    update_status - writes the status pane "(%2d,%2d) Current:"
    run - the main event loop, interprets the movement, write, quit
'''
import curses
import curses.textpad
import sys
import os
from os import path
from FramedWindow import FramedWindow
from Cell import Cell

class PainterWindow:
    def __init__(self, fileName, stdscr):
        self.current_char='.'
        self.grid=[]
        self.cursor_row = 0
        self.cursor_col = 0
        self.outfile=fileName
        self.stdscr=stdscr
        allowed_chars_set=set(".#/\\")
        if os.path.exists(fileName) and os.path.getsize(fileName)!=0:
            
            with open(fileName, "r") as f:
                filegrid=list()
                for line in f:
                    line = line.strip('\n')
                    filegrid.append(line)
                    if not set(line) <= allowed_chars_set:
                        raise Exception("Invalid characters in file.")
                for i in range(0,len(filegrid)):
                    if len(filegrid[i]) != len(filegrid[0]):
                        raise Exception("Inconsistent row lengths.")
            self.file_width=len(max(filegrid))*2
            self.file_height=len(filegrid)
            if self.file_height > curses.LINES-5 or self.file_width > curses.COLS-1:
                raise Exception("File size is too large for terminal size")
            f.close()

            # self.mainpane = FramedWindow(curses.LINES-5, curses.COLS-1, 0, 0)
            # self.statuspane = FramedWindow(3, curses.COLS-1, curses.LINES-5, 0)
            self.mainpane = FramedWindow(self.file_height+2, self.file_width+2, 0, 0)
            self.statuspane = FramedWindow(3, self.file_width+2, self.file_height+2, 0)
            
            for row in range(len(filegrid)):
                self.grid.append(list())
                for col in range(len(filegrid[0])):
                    self.grid[row].append(Cell(row, col, filegrid[row][col], self.mainpane))
                    self.grid[row][col].draw()
            self.height=len(filegrid)
            self.width=len(filegrid[0])
        else:
            self.mainpane = FramedWindow(curses.LINES-5, curses.COLS-1, 0, 0)
            self.statuspane = FramedWindow(3, curses.COLS-1, curses.LINES-5, 0)
            for row in range(0,self.mainpane.height-2):
                self.grid.append(list())
                for col in range(0,int(self.mainpane.width//2-1)):   #across
                    self.grid[row].append(Cell(row,col,'#',self.mainpane))
                    self.grid[row][col].draw()
            self.height=self.mainpane.height-2
            self.width=int(self.mainpane.width//2-1)


    def toggle_glyph(self):
        if self.current_char == '.':
            self.current_char='/'
        elif self.current_char == '/':
            self.current_char='\\'
        elif self.current_char == '\\':
            self.current_char='#'
        elif self.current_char == '#':
            self.current_char='.'
        self.update_status()

    #writes the status pane "(%2d,%2d) Current:""
    def update_status(self):
        myString = "(%2d,%2d) Current: " % (self.cursor_col, self.cursor_row)
        self.statuspane.write(myString,0,0)
        self.statuspane.plot(16,0,Cell.glyph[self.current_char].lhs, Cell.glyph[self.current_char].color_pair)
        self.statuspane.plot(17,0,Cell.glyph[self.current_char].rhs, Cell.glyph[self.current_char].color_pair)

    #run the main event loop, interprets movement, write, quit
    def run(self): 
        curses.curs_set(0)
        self.grid[self.cursor_row][self.cursor_col].cursor_on()
        self.mainpane.redraw()
        self.update_status()
        self.statuspane.redraw()
        self.stdscr.refresh()
        while True:
            # key = self.stdscr.getkey()
            key = self.mainpane.window.getch()
            key=chr(key)
            if key == 'Q':
                break
            if key == 'j' or key =='J':
                self.grid[self.cursor_row][self.cursor_col].cursor_off()
                if key == 'J':
                    self.grid[self.cursor_row][self.cursor_col].change_char(self.current_char)
                if self.cursor_row < self.height-1:
                    self.cursor_row+=1
                self.grid[self.cursor_row][self.cursor_col].cursor_on()
                #move down
            elif key == 'k' or key == 'K':
                self.grid[self.cursor_row][self.cursor_col].cursor_off()
                if key == 'K':
                    self.grid[self.cursor_row][self.cursor_col].change_char(self.current_char)
                if self.cursor_row > 0:
                    self.cursor_row-=1
                self.grid[self.cursor_row][self.cursor_col].cursor_on()
            #     #move up
            elif key == 'h' or key == 'H':
                self.grid[self.cursor_row][self.cursor_col].cursor_off()
                if key == 'H':
                    self.grid[self.cursor_row][self.cursor_col].change_char(self.current_char)
                if self.cursor_col > 0:
                    self.cursor_col-=1
                self.grid[self.cursor_row][self.cursor_col].cursor_on()
                #move left
            elif key == 'l' or key == 'L':
                self.grid[self.cursor_row][self.cursor_col].cursor_off()
                if key == 'L':
                    self.grid[self.cursor_row][self.cursor_col].change_char(self.current_char)
                if self.cursor_col < self.width-1:
                    self.cursor_col+=1
                self.grid[self.cursor_row][self.cursor_col].cursor_on()
                #move right
            elif key == ' ':
                self.toggle_glyph()
            elif key == 'w' or key == 's':
                #save file
                save_window=FramedWindow(3, 25, self.mainpane.height//2-2, self.mainpane.width//2-10)
                save_window.write("Save to file",-1,save_window.width//2-8)
                save_sub_window=save_window.window.subwin(save_window.height-2,save_window.width-2,self.mainpane.height//2,self.mainpane.width//2-8)
                save_window.redraw()

                curses.curs_set(True)
                self.stdscr.refresh()
                # save_window.window.move(1,1)
                save=curses.textpad.Textbox(save_sub_window)
                save.stripspaces = True
                save_sub_window.addstr(0,0,self.outfile)
                myFile=save.edit()
                self.outfile=myFile.strip()
                # self.statuspane.write(myFile,0,1)
                self.statuspane.redraw()
                del save
                del save_window
                output=open(self.outfile, 'w+')
                for row in range(self.height):
                    for col in range(self.width):
                        output.write(self.grid[row][col].character)
                    if(row < self.height-1):
                        output.write('\n')
                self.stdscr.refresh()
                curses.curs_set(False)
            self.update_status()
            self.mainpane.redraw()
        
        
    '''
    for row in range(len(filegrid)):
      self.grid.append(list())
      for col in range(len(filegrid[0])):
        self.grid[row].append(Cell(row, col, filegrid[row][col], self.mainpane))
    '''