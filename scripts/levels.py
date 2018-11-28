from graphics import *
from screen import *
from blocks import *
import gameStates as state
import common_variables as var

def drawLevel(win, level):
    if level == 1:
        drawLevel1(win)
    elif level == 2:
        drawLevel2(win)
    elif level == 3:
        drawLevel3(win)
    
    # while True:
    #     update(state.FPS)
        
def drawLevel1(win):
    drawPlayScreen(win)
    for col in range(10):
        for row in range(10):
            x1 = var.side_offset + row * var.block_width
            y1 = var.top_offset + col * var.block_height
            x2 = x1 + var.block_width
            y2 = y1 + var.block_height
            addBlock(win, Point(x1, y1), Point(x2, y2))
            
def drawLevel2(win):
    drawPlayScreen(win)
    for col in range(10):
        for row in range(10 - col):
            x1 = var.side_offset + (var.block_width / 2 * col) + row * var.block_width
            y1 = var.top_offset + col * var.block_height
            x2 = x1 + var.block_width
            y2 = y1 + var.block_height
            addBlock(win, Point(x1, y1), Point(x2, y2))
            
def drawLevel3(win):
    drawPlayScreen(win)
    aux = 8
    for row in range(10):
        for col in range(10 - aux):
            x1 = var.side_offset + row * var.block_width
            y1 = var.top_offset + (aux/2 * var.block_height) + col * var.block_height
            x2 = x1 + var.block_width
            y2 = y1 + var.block_height
            addBlock(win, Point(x1, y1), Point(x2, y2))
        if row < 4:
            aux -= 2
        elif row >= 5:
            aux += 2
        
        
#drawPlayer() after drawing a level