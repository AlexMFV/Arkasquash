import common as var
from graphics import *

def removeHeart(gameVars):
    gameVars[var.lives] -= 1
    
def addHeart():
    gameVars[var.lives] += 1
    
def drawHearts(win, game):
    if game[var.lives] <= 3 and game[var.lives] > 0:
        game[var.livesImage].undraw()
        game[var.livesImage] = Image(Point(700, 715), "../../resources/" + var.hearts[game[var.lives]-1] + ".gif")
        game[var.livesImage].draw(win)
        game[var.livesText].undraw()
    else:
        if game[var.lives] > 3:
            game[var.livesImage] = Image(Point(710, 715), "../../resources/one.gif")
            game[var.livesImage].draw(win)
            game[var.livesText].setText(var.lives)
            game[var.livesText].setSize(24)
            game[var.livesText].setTextColor("lime")
            game[var.livesText].draw(win)
        else:
            game[var.livesImage].undraw()