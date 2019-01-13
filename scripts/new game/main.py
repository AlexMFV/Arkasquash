from graphics import *
from menu import mainMenu
from levels import *
import common as var
import states
from game import *

def main():
    win = GraphWin("Arkasquash - Alexandre Valente", 800, 800, autoflush=False) #, autoflush=True
    startApplication(win)
    win.close()
    
def startApplication(win):
    gameVariables = [1, 0, 0, 0, 0, 3, [], [], Text(Point(690, 715), ""), 0] #Player is appended later
    
    hasExited = False
    state = states.MAIN_MENU
    
    while not hasExited:
        if state == states.MAIN_MENU:
            state = mainMenu(win, state)
            
        elif state == states.GAME_STARTED:
            state = playGame(win, state, gameVariables)
            
        elif state == states.GAME_ENDED: #When the game ends, prompt the user with the scores, or save score
            state = saveScore(win, state, gameVariables)
            
        elif state == states.HIGH_SCORES:
            state = highScores(win, state)
            
        elif state == states.INST_MENU:
            state = instructionsMenu(win, state)
            
        elif state == states.LEVEL_EDITOR:
            state = levelEditor(win, state)
            
        elif state == states.CARACTER_SEL:
            state = caracterSelection(win, state)
            
        elif state == states.GAME_EXIT or win.closed:
            hasExited = True
            
        update(states.FPS)

def playGame(win, state, gameVariables):
    '''Draws the playing level, according to the current level number'''
    drawLevel(win, gameVariables)
    hasStarted = True
    isPlaying = False
    speed = 50
    ballSpeed = 5
    ballDir = -1
    
    '''Game Loop'''
    while hasStarted:
        key = win.checkKey()
        
        if key == 'space' and not isPlaying:
            isPlaying = True
            ballDir = startBall()

        if key == 'Left' or key == 'Right':
            movePlayer(win, key, gameVariables[var.player], speed)
            
        if not isPlaying:
            if gameVariables[var.ball].getCenter().getX() != gameVariables[var.player].getAnchor().getX():
                x = gameVariables[var.player].getAnchor().getX() - gameVariables[var.ball].getCenter().getX()
                gameVariables[var.ball].move(x, 0)
            
        if isPlaying and dir != -1:
            ballDir = checkCollisions(ballDir, gameVariables, var.ball_rad)
            moveBall(ballDir, ballSpeed, gameVariables)
        elif isPlaying and dir == 1:
            loseLife(gameVariables)
            isPlaying = restartGame()
        
        if gameVariables[var.lives] < 0:
            isPlaying = False
    
        update(states.FPS)
        
    return states.GAME_ENDED

main()