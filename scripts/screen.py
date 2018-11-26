from graphics import *
import random as rand

def drawPlayScreen(win):
    undrawAll(win)
    '''Score, Powers, Extras and Lives Tab'''
    rightTab = Image(Point(700, 400), "../resources/rightTab.gif")
    rightTab.draw(win)
    # rightTab = Rectangle(Point(600,0), Point(800, 800))
    # rightTab.setWidth(0)
    # rightTab.setFill("grey")
    # rightTab.draw(win)
    
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
        i.undraw(win)