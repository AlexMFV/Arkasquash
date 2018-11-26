from graphics import *
from screen import *

def main():
    win = GraphWin("Arkasquash by Alexandre Valente UP902282", 800, 800)
    drawPlayScreen(win)
    win.getMouse()
    win.close()
    
main()