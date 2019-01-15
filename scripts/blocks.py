from graphics import *
import common as var
import random as rand
import lives as l

def addBlock(win, pos1, pos2, gameVariables):
    gameVariables[var.blocks].append(Rectangle(pos1, pos2))
    gameVariables[var.blockColors].append(randomColor())
    drawBlock(win, -1, gameVariables[var.blocks], gameVariables[var.blockColors])
    
def addPoints(win, idx, gameVars):
    if gameVars[var.blockColors][idx] == "red":
        scoreToAdd = 50
    elif gameVars[var.blockColors][idx] == "green":
        scoreToAdd = 100
    elif gameVars[var.blockColors][idx] == "blue":
        scoreToAdd = 150
    else:
        scoreToAdd = 1000
        
    if gameVars[var.rockets] <= 3:
        gameVars[var.rockets] += getRocket()
        l.drawRockets(win, gameVars)
    
    gameVars[var.score] += scoreToAdd
    l.updateScore(gameVars)
    
def getRocket():
    value = rand.randint(0, 1000)
    if value >= 0 and value < 100:
        return 1
    else:
        return 0

def removeBlock(idx, gameVars):
    gameVars[var.blocks][idx].undraw()
    del gameVars[var.blocks][idx]
    
def removeBlockRaw(obj, gameVars):
    idx = gameVars[var.blocks].index(obj)
    gameVars[var.blocks][idx].undraw()
    gameVars[var.blocks].remove(obj)
    
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
        
def moveBlocksDown(win, gameVariables):
    for b in gameVariables[var.blocks]:
        b.move(0, 10)