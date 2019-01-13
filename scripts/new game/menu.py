from graphics import *
import states

def mainMenu(win, state):
    '''Draw the MainMenu Buttons, Background and Animations'''
    drawMainMenu(win)
    
    '''Detect presses on the MainMenu Buttons'''
    while state == states.MAIN_MENU:
        clicked = win.checkMouse()
        
        if clicked != None:
            if pressedPlay(clicked):
                state = states.GAME_STARTED
                
            elif pressedHighScores(clicked):
                state = states.HIGH_SCORES
                
            elif pressedInstructions(clicked):
                state = states.INST_MENU
                
            elif pressedLevelEditor(clicked):
                state = states.LEVEL_EDITOR
                
            elif pressedCharSelection(clicked):
                state = states.CARACTER_SEL
                
            elif pressedExit(clicked):
                state = states.GAME_EXIT
                
        #updateMenuAnimation(win)
    return state

def drawMainMenu(win):
    logo = Image(Point(400, 100), "../../resources/Arka.gif")
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