from graphics import *
from screen import *
from levels import *
import common_variables as var

def main():
    win = GraphWin("Arkasquash by Alexandre Valente UP902282", 800, 800, autoflush=False)
    drawLevel(win, var.level_num)
    win.getMouse()
    win.close()
    
main()