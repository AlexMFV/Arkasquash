import common as var
from graphics import *
import blocks as bl
import states
from sound import *
import threading

def removeHeart(gameVars):
    thread = threading.Thread(target=playDeath)
    thread.start() #Sound when the player dies
    gameVars[var.lives] -= 1
    
def addHeart():
    gameVars[var.lives] += 1
    
def drawHearts(win, game):
    if game[var.lives] <= 3 and game[var.lives] > 0:
        game[var.livesImage].undraw()
        game[var.livesImage] = Image(Point(700, 715), "../resources/" + var.hearts[game[var.lives]-1] + ".gif")
        game[var.livesImage].draw(win)
        game[var.livesText].undraw()
    else:
        if game[var.lives] > 3:
            game[var.livesImage] = Image(Point(710, 715), "../resources/one.gif")
            game[var.livesImage].draw(win)
            game[var.livesText].setText(var.lives)
            game[var.livesText].setSize(24)
            game[var.livesText].setTextColor("lime")
            game[var.livesText].draw(win)
        else:
            game[var.livesImage].undraw()
            
def drawRockets(win, game):
    if game[var.rockets] >= 1 and game[var.rockets] <= 3:
        game[var.rocketImage].undraw()
        game[var.rocketImage] = Image(Point(700, 270), "../resources/r" + var.hearts[game[var.rockets]-1] + ".gif")
        game[var.rocketImage].draw(win)
    else:
        if game[var.rockets] < 1:
            game[var.rocketImage].undraw()
        else:
            game[var.rockets] = 3
            
def drawScore(win, game):
    game[var.scoreText].setTextColor("lime")
    game[var.scoreText].setSize(22)
    game[var.scoreText].setText("0")
    game[var.scoreText].draw(win)
    
def updateScore(game):
    game[var.scoreText].setText(game[var.score])
    
def launchRocket(win, game):
    game[var.rocketL] = Image(Point(game[var.player].getAnchor().getX(), game[var.player].getAnchor().getY() - 20), "../resources/bullets.gif")
    game[var.rocketL].draw(win)
    
def moveRocket(win, game):
    y = game[var.rocketL].getAnchor().getY()
    
    if checkExplosion(win, game, y):
        return False
    
    if y > 0:
        game[var.rocketL].move(0, -8)
        return True #if is alive, or False if exploded or leave screen
    else:
        game[var.rocketL].undraw()
        return False
    
def checkExplosion(win, game, y):
    blocks = game[var.blocks]
    x = game[var.rocketL].getAnchor().getX()
    y = y - 10
    
    for b in blocks:
        if x >= b.getP2().getX() - var.block_width and x <= b.getP2().getX():
            if y >= b.getP2().getY() - 8 and y <= b.getP2().getY():
                explodeRocket(win, game, 50, x, y+10)
                return True
    return False

def explodeRocket(win, game, rad, x, y):
    aux = 0
    blcks = game[var.blocks]
    for b in blcks:
        if checkInside(x-rad, y-rad, x+rad, y+rad, b.getP1().getX(), b.getP1().getY()):
            bl.addPointsRaw(win, aux, game)
            bl.removeBlockRaw(b, game)
        elif checkInside(x-rad, y-rad, x+rad, y+rad, b.getP1().getX(), b.getP2().getY()):
            bl.addPointsRaw(win, aux, game)
            bl.removeBlockRaw(b, game)
        elif checkInside(x-rad, y-rad, x+rad, y+rad, b.getP2().getX(), b.getP1().getY()):
            bl.addPointsRaw(win, aux, game)
            bl.removeBlockRaw(b, game)
        elif checkInside(x-rad, y-rad, x+rad, y+rad, b.getP2().getX(), b.getP2().getY()):
            bl.addPointsRaw(win, aux, game)
            bl.removeBlockRaw(b, game)
    game[var.rocketL].undraw()
    
def checkInside(x, y, x2, y2, bx, by):
    if bx >= x and bx <= x2:
        if by >= y and by <= y2:
            return True
        else:
            return False
    else:
        return False
    