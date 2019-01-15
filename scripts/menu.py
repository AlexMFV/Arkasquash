from graphics import *
import states
from pathlib import *

def mainMenu(win, state):
    '''Draw the MainMenu Buttons, Background and Animations'''
    drawMainMenu(win)
    
    '''Detect presses on the MainMenu Buttons'''
    while state == states.MAIN_MENU:
        clicked = win.getMouse() #Bug with checkMouse(), ghosting?
        
        if clicked != None:
            if pressedPlay(clicked):
                state = states.GAME_STARTED
                
            elif pressedHighScores(clicked):
                state = states.HIGH_SCORES
                
            elif pressedInstructions(clicked):
                state = states.INST_MENU
                
            #elif pressedLevelEditor(clicked):
                #state = states.LEVEL_EDITOR
                
            elif pressedCharSelection(clicked):
                state = states.CARACTER_SEL
                
            elif pressedExit(clicked):
                state = states.GAME_EXIT
                
    return state

def drawMainMenu(win):
    back = Image(Point(400, 400), "../resources/background.gif")
    back.draw(win)
    logo = Image(Point(400, 125), "../resources/Arka.gif")
    logo.draw(win)
    logo2 = Image(Point(400, 300), "../resources/Squash.gif")
    logo2.draw(win)
    drawMenuButtons(win)
    
def drawMenuButtons(win):
    playBtn = Image(Point(150, 500), "../resources/play.gif")
    playBtn.draw(win)
    #playBtn = Image(Point(400, 500), "../resources/editor.gif")
    #playBtn.draw(win)
    playBtn = Image(Point(650, 500), "../resources/tutorial.gif")
    playBtn.draw(win)
    playBtn = Image(Point(150, 650), "../resources/scores.gif")
    playBtn.draw(win)
    playBtn = Image(Point(400, 650), "../resources/player.gif")
    playBtn.draw(win)
    playBtn = Image(Point(650, 650), "../resources/exit.gif")
    playBtn.draw(win)
    
def drawInstructions(win):
    inst = Image(Point(400, 400), "../resources/instructions.gif")
    inst.draw(win)
    return inst

def drawDesign(win):
    tab = Image(Point(400, 400), "../resources/design.gif")
    tab.draw(win)
    return tab

def drawPlayerDesign(win):
    path = Path("player.txt")
    
    if not path.is_file():
        file = open("player.txt", "w")
        file.write("p1")
        file.close()

    inFile = open("player.txt", "r+")
    data = inFile.read()
    inFile.close()
    
    if data != "p1" and data != "p2" and data != "p3" and data != "p4":
        data = "p1"
        
    player = Image(Point(395, 425), "../resources/" + data + ".gif")
    player.draw(win)
    return int(data.split('p')[1]), player
    
def minusDesign(n, player, win):
    player.undraw()
    
    n -= 1
    if n < 1:
        n = 4
        
    player = drawPlayerDesignNumber(n, win)
    return n, player
    
def plusDesign(n, player, win):
    player.undraw()
    
    n += 1
    if n > 4:
        n = 1
        
    player = drawPlayerDesignNumber(n, win)
    return n, player
    
def saveDesign(n):
    file = open("player.txt", "w+")
    file.write("p" + str(n))
    file.close()
    
def drawPlayerDesignNumber(n, win):
    player = Image(Point(395, 425), "../resources/p" + str(n) + ".gif")
    player.draw(win)
    return player
    
'''Check for all the pressed in the Menu Buttons'''   
def pressedPlay(clickPos):
    if clickPos.getY() >= 450 and clickPos.getY() <= 550:
        if clickPos.getX() >= 50 and clickPos.getX() <= 250:
            return True
    return False
    
def pressedLevelEditor(clickPos):
    if clickPos.getY() >= 450 and clickPos.getY() <= 550:
        if clickPos.getX() >= 300 and clickPos.getX() <= 500:
            return True
    return False
    
def pressedInstructions(clickPos):
    if clickPos.getY() >= 450 and clickPos.getY() <= 550:
        if clickPos.getX() >= 550 and clickPos.getX() <= 750:
            return True
    return False
    
def pressedHighScores(clickPos):
    if clickPos.getY() >= 600 and clickPos.getY() <= 700:
        if clickPos.getX() >= 50 and clickPos.getX() <= 250:
            return True
    return False
    
def pressedCharSelection(clickPos):
    if clickPos.getY() >= 600 and clickPos.getY() <= 700:
        if clickPos.getX() >= 300 and clickPos.getX() <= 500:
            return True
    return False
    
def pressedExit(clickPos):
    if clickPos.getY() >= 600 and clickPos.getY() <= 700:
        if clickPos.getX() >= 550 and clickPos.getX() <= 750:
            return True
    return False