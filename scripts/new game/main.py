from graphics import *
from menu import mainMenu
from levels import *
import common as var
import states
from game import *
import lives as l

def main():
    win = GraphWin("Arkasquash - Alexandre Valente", 800, 800, autoflush=False) #, autoflush=True
    startApplication(win)
    win.close()
    
def startApplication(win):
    gameVariables = [1, 0, 0, 0, 0, 3, [], [], Text(Point(690, 715), ""), Image(Point(0,0), "")] #Player is appended later
    
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
    l.drawHearts(win, gameVariables)
    
    '''Game Loop'''
    while hasStarted:
        key = win.checkKey()
        
        '''Game hasnt started, waiting for player to start'''
        if key == 'space' and not isPlaying:
            isPlaying = True
            ballDir = startBall()

        '''Move player Paddle'''
        if key == 'Left' or key == 'Right':
            movePlayer(win, key, gameVariables[var.player], speed)
        
        '''Move the paddle, while the game has not started'''
        if not isPlaying:
            if gameVariables[var.ball].getCenter().getX() != gameVariables[var.player].getAnchor().getX():
                x = gameVariables[var.player].getAnchor().getX() - gameVariables[var.ball].getCenter().getX()
                gameVariables[var.ball].move(x, 0)
            if gameVariables[var.ball].getCenter().getY() >= 750:
                gameVariables[var.ball].move(0, -10)
        
        '''Detect collisions, ball movement, when die lose live and manage hearts'''
        if isPlaying and ballDir != -1:
            ballDir = checkCollisions(ballDir, gameVariables, var.ball_rad)
            moveBall(ballDir, ballSpeed, gameVariables)
        elif isPlaying and ballDir == -1:
            l.removeHeart(gameVariables)
            l.drawHearts(win, gameVariables)
            isPlaying = False
          
        '''When the number of blocks reaches 0, start next level and add heart'''
        if isPlaying and len(gameVariables[var.blocks]) <= 0:
            nextLevel(gameVariables)
            drawLevel(win, gameVariables)
            l.drawHearts(win, gameVariables)
            isPlaying = False
            ballDir = -1
            
        if gameVariables[var.level] > 3:
            hasStarted = False
    
        '''When all lives are lost, end the game'''
        if gameVariables[var.lives] <= 0:
            isPlaying = False
            hasStarted = False
    
        update(states.FPS)
        
    return states.GAME_ENDED

main()