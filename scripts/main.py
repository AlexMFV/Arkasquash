from graphics import *
import gameStates as state
from levels import drawLevel

from menu import mainMenu

def main():
    win = GraphWin("Arkasquash - Alexandre Valente", 800, 800, autoflush=False)
    startApplication(win)
    win.close()
    
def startApplication(win):
    hasExited = False
    gameController = state.MAIN_MENU
    
    while not hasExited:
        if gameController == state.MAIN_MENU:
            gameController = mainMenu(win, gameController)
            
        elif gameController == state.GAME_STARTED:
            gameController = playGame(win, gameController)
            
        elif gameController == state.HIGH_SCORES:
            gameController = highScores(win, gameController)
            
        elif gameController == state.INST_MENU:
            gameController = instructionsMenu(win, gameController)
            
        elif gameController == state.LEVEL_EDITOR:
            gameController = levelEditor(win, gameController)
            
        elif gameController == state.CARACTER_SEL:
            gameController = caracterSelection(win, gameController)
            
        elif gameController == state.GAME_EXIT or win.closed:
            hasExited = True
            
        #update(state.FPS)
    
main()