from graphics import *

def mainMenu(win, gameController):
    '''Draw the MainMenu Buttons, Background and Animations'''
    drawMainMenu(win)
    
    '''Detect presses on the MainMenu Buttons'''
    while gameController == state.MAIN_MENU:
        clicked = win.checkMouse()
        
        if clicked != None:
            if pressedPlay(clickPos):
                gameController = state.GAME_STARTED
                
            elif pressedHighScores(clickPos):
                gameController = state.HIGH_SCORES
                
            elif pressedInstructions(clickPos):
                gameController = state.INST_MENU
                
            elif pressedLevelEditor(clickPos):
                gameController = state.LEVEL_EDITOR
                
            elif pressedCharSelection(clickPos):
                gameController = state.CARACTER_SEL
                
            elif pressedExit(clickPos):
                gameController = state.GAME_EXIT
                
        updateMenuAnimation(win)

def drawMainMenu(win):