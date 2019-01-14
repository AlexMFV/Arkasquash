import states
import common as var
from graphics import *
import random as rand
from blocks import *

def drawLevel(win, gameVariables):
    if gameVariables[var.level] == 1:
        drawLevel1(win, gameVariables)
    elif gameVariables[var.level] == 2:
        drawLevel2(win, gameVariables)
    elif gameVariables[var.level] == 3:
        drawLevel3(win, gameVariables)
    
    drawPlayer(win, gameVariables, getPlayerType())
    drawBall(win, gameVariables)
    # while True:
    #     update(state.FPS)
    
def nextLevel(gameVars):
    if gameVars[var.level] < 3:
        gameVars[var.level] += 1
    
    gameVars[var.lives] += 1
        
def drawLevel1(win, gameVariables):
    drawPlayScreen(win)
    for col in range(9, 4, -1):
        for row in range(10):
            x1 = var.side_offset + row * var.block_width
            y1 = var.top_offset + col * var.block_height
            x2 = x1 + var.block_width
            y2 = y1 + var.block_height
            addBlock(win, Point(x1, y1), Point(x2, y2), gameVariables)
            
def drawLevel2(win, gameVariables):
    drawPlayScreen(win)
    for col in range(10):
        for row in range(10 - col):
            x1 = var.side_offset + (var.block_width / 2 * col) + row * var.block_width
            y1 = var.top_offset + col * var.block_height
            x2 = x1 + var.block_width
            y2 = y1 + var.block_height
            addBlock(win, Point(x1, y1), Point(x2, y2), gameVariables)
            
def drawLevel3(win, gameVariables):
    drawPlayScreen(win)
    aux = 8
    for row in range(10):
        for col in range(10 - aux):
            x1 = var.side_offset + row * var.block_width
            y1 = var.top_offset + (aux/2 * var.block_height) + col * var.block_height
            x2 = x1 + var.block_width
            y2 = y1 + var.block_height
            addBlock(win, Point(x1, y1), Point(x2, y2), gameVariables)
        if row < 4:
            aux -= 2
        elif row >= 5:
            aux += 2
            
def drawPlayScreen(win):
    undrawAll(win)
    '''Score, Powers, Extras and Lives Tab'''
    rightTab = Image(Point(700, 400), "../../resources/RightTab.gif")
    rightTab.draw(win)
    
    '''Draws the Play Area itself'''
    leftTab = Rectangle(Point(0, 0), Point(600, 800))
    leftTab.setWidth(0)
    leftTab.setFill("black")
    leftTab.draw(win)
    
    '''Draws random dots in the screen just for effects'''
    drawStars(win)
    
def drawStars(win):
    for i in range(1000):
        x = rand.randint(0, 600-1)
        y = rand.randint(0, 800-1)
        '''Draws the pixel at the coordinate and the color provided'''
        win.plotPixel(x, y, "white")
        
def undrawAll(win):
    for i in win.items:
        i.undraw()
        
def drawPlayer(win, gameVariables, type):
    #box = Rectangle(Point(250, 770), Point(350, 790))
    box = Image(Point(300, 780), "../../resources/"+ type + ".gif")
    #box.setFill("green")
    #box.setOutline("White")
    box.draw(win)
    gameVariables.append(box)
    
def drawBall(win, vars):
    ball = Circle(Point(vars[var.player].getAnchor().getX(),
    vars[var.player].getAnchor().getY() - 20), var.ball_rad)
    ball.setFill("purple")
    ball.setOutline("white")
    ball.draw(win)
    vars.append(ball)
    
def getPlayerType():
    return "p1"
    
def drawInitialGame(win, gameVars, lives):
    gameVars[var.livesImage] = Image(Point(690, 715), var.hearts[gameVars[var.lives]-1])
    gameVars[var.livesImage].draw(win)
    
    