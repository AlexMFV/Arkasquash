from graphics import *
import common as var
import random as rand

def addBlock(win, pos1, pos2, gameVariables):
    gameVariables[var.blocks].append(Rectangle(pos1, pos2))
    gameVariables[var.blockColors].append(randomColor())
    drawBlock(win, -1, gameVariables[var.blocks], gameVariables[var.blockColors])
    
def addPoints(idx, gameVars):
    if gameVars[var.blockColors][idx] == "red":
        scoreToAdd = 50
    elif gameVars[var.blockColors][idx] == "green":
        scoreToAdd = 100
    elif gameVars[var.blockColors][idx] == "blue":
        scoreToAdd = 150
    else:
        scoreToAdd = 1000
    
    gameVars[var.score] += scoreToAdd
    #del gameVars[var.blockColors][idx]

def removeBlock(idx, gameVars):
    gameVars[var.blocks][idx].undraw()
    del gameVars[var.blocks][idx]
    
def drawBlock(win, idx, blocks, block_colors):
    rect = blocks[idx]
    rect.setFill(block_colors[idx])
    rect.setWidth(var.block_outline)
    rect.setOutline(var.outlineColor)
    rect.draw(win)
    
colors = ["red", "green", "blue", "gold"]

def randomColor():
    value = rand.randint(0, 1000)
    if value >= 0 and value < 500:
        return colors[0]
    elif value >= 500 and value < 800:
        return colors[1]
    elif value >= 800 and value < 999:
        return colors[2]
    else:
        return colors[3]