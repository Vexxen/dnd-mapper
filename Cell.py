'''
Cell.py - handles the arithmetic to compensate for 2 characters for each position
    Methods:
        init - takes a row & column, character, and parent window, draws itself
        at location:    (row,col*2, and row, col*2+1)
        cursor_on - turns on the 2 characters for given position
        cursor_off - turns off the 2 characters for given position
        change_char - change the character
        draw - calls plot on the parent window
'''
import curses
import collections
class Cell:

    Glyph=collections.namedtuple('Glyph', ['lhs','rhs','color_pair'])
    glyph=dict()
    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE) # cursor
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK) # earth
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE) # hall
    glyph['.']=Glyph('[', ']', curses.color_pair(3))
    glyph['#']=Glyph(curses.ACS_CKBOARD, curses.ACS_CKBOARD, curses.color_pair(2))
    glyph['/']=Glyph('/', ']', curses.color_pair(3))
    glyph['\\']=Glyph('\\', ']', curses.color_pair(3))


    #takes a row & column, character, and parent window and draws itself at (row,col*2, and row,col*2+1)
    def __init__(self, row, col, myChar, parentWindow):
        self.row=row
        self.column=col
        self.character=myChar
        self.parent=parentWindow
        # curses.addch()
    # #turns on the 2 characters for given position
    def cursor_on(self):
        self.parent.plot(self.column*2,self.row, Cell.glyph[self.character].lhs, curses.color_pair(1))
        self.parent.plot(self.column*2+1,self.row, Cell.glyph[self.character].rhs, curses.color_pair(1))
    # #turns off the 2 characters for given position
    def cursor_off(self):  
        self.parent.plot(self.column*2,self.row, Cell.glyph[self.character].lhs, self.glyph[self.character].color_pair|curses.A_NORMAL)
        self.parent.plot(self.column*2+1,self.row, Cell.glyph[self.character].rhs, self.glyph[self.character].color_pair|curses.A_NORMAL)

    # #change the character
    def change_char(self, newChar):
        self.character=newChar
        self.draw()

    # #calls plot on the parent window
    def draw(self):
        self.parent.plot(self.column*2, self.row, self.glyph[self.character].lhs, self.glyph[self.character].color_pair)
        self.parent.plot(self.column*2+1, self.row, self.glyph[self.character].rhs, self.glyph[self.character].color_pair)
        