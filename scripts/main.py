from graphics import *
import gameStates as state

def main():
    win = GraphWin("Arkasquash - Alexandre Valente", 800, 800, autoflush=False)
    startApplication(win)
    win.close()
    
def startApplication(win):
    hasExited = False
    gameController = state.MAIN_MENU
    
    while not hasExited:
        if gameController == state.MAIN_MENU:
            mainMenu(win, gameController)
            
        elif gameController == state.GAME_STARTED:
            playGame(win, gameController)
            
        elif gameController == state.HIGH_SCORES:
            highScores(win, gameController)
            
        elif gameController == state.INST_MENU:
            instructionsMenu(win, gameController)
            
        elif gameController == state.LEVEL_EDITOR:
            levelEditor(win, gameController)
            
        elif gameControler == state.CARACTER_SEL:
            caracterSelection(win, gameController)
            
        elif gameController == state.GAME_EXIT or win.close()
            hasExited = True
            
        #update(state.FPS)
    
main()