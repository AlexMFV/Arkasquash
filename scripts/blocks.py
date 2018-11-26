from graphics import *
from colors import *
import common_variables as var

def addBlock(win, pos1, pos2):
    var.blocks.append(Rectangle(pos1, pos2))
    var.block_colors.append(randomColor())
    drawBlock(win, -1)
    
def removeBlock(idx):
    blocks[idx].undraw(win)
    del blocks[idx]
    
def drawBlock(win, idx):
    rect = var.blocks[idx]
    rect.setFill(var.block_colors[idx])
    rect.setWidth(var.block_outline)
    rect.setOutline(var.outlineColor)
    rect.draw(win)