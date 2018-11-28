from graphics import *
import gameStates as state
import colors as color

def mainMenu(win, gameController):
    '''Draw the MainMenu Buttons, Background and Animations'''
    drawMainMenu(win)
    
    '''Detect presses on the MainMenu Buttons'''
    while gameController == state.MAIN_MENU:
        clicked = win.checkMouse()
        
        if clicked != None:
            if pressedPlay(clicked):
                gameController = state.GAME_STARTED
                
            elif pressedHighScores(clicked):
                gameController = state.HIGH_SCORES
                
            elif pressedInstructions(clicked):
                gameController = state.INST_MENU
                
            elif pressedLevelEditor(clicked):
                gameController = state.LEVEL_EDITOR
                
            elif pressedCharSelection(clicked):
                gameController = state.CARACTER_SEL
                
            elif pressedExit(clicked):
                gameController = state.GAME_EXIT
                
        #updateMenuAnimation(win)
    return gameController

def drawMainMenu(win):
    logo = Image(Point(400, 100), "../resources/Arka.gif")
    logo.draw(win)
    #drawMenuText(win)
    drawMenuButtons(win)
    
def drawMenuButtons(win):
    playBtn = Rectangle(Point(50, 450), Point(250, 550))
    playBtn.draw(win)
    playBtn = Rectangle(Point(300, 450), Point(500, 550))
    playBtn.draw(win)
    playBtn = Rectangle(Point(550, 450), Point(750, 550))
    playBtn.draw(win)
    playBtn = Rectangle(Point(50, 600), Point(250, 700))
    playBtn.draw(win)
    playBtn = Rectangle(Point(300, 600), Point(500, 700))
    playBtn.draw(win)
    playBtn = Rectangle(Point(550, 600), Point(750, 700))
    playBtn.draw(win)
#def drawButtonFrame(win, pos1, pos2):
    

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