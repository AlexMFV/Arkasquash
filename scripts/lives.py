import common_variables as var
from graphics import *

def removeHeart():
    var.lives -= 1
    
def addHeart():
    var.lives += 1
    
def drawHearts(win):
    if var.lives <= 3 and var.lives > 0:
        if var.livesImage != 0:
            var.livesImage.undraw()
        var.livesImage = Image(Point(700, 715), "../resources/" + var.hearts[var.lives-1] + ".gif")
        var.livesImage.draw(win)
        var.livesText.undraw()
    else:
        var.livesImage = Image(Point(710, 715), "../resources/one.gif")
        var.livesImage.draw(win)
        var.livesText.setText(var.lives)
        var.livesText.setSize(24)
        var.livesText.setTextColor("lime")
        var.livesText.draw(win)