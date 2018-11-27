from graphics import *
from screen import *
from levels import *
import common_variables as var
import lives as l

def main():
    win = GraphWin("Arkasquash by Alexandre Valente", 800, 800, autoflush=False)
    drawLevel(win, var.level_num)
    win.getMouse()
    win.close()
    
main()