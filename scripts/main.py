from graphics import *
from menu import *
from levels import *
import common as var
import states
from game import *
import lives as l
from pathlib import *
from file import *
from highscores import *

def main():
    win = GraphWin("Arkasquash by Alexandre Valente", 800, 800, autoflush=False) #, autoflush=True
    startApplication(win)
    win.close()
    
def startApplication(win):
    hasExited = False
    state = states.MAIN_MENU
    
    while not hasExited:
        if state == states.MAIN_MENU:
            state = mainMenu(win, state)
            
        elif state == states.GAME_STARTED:
            state, gameVariables = playGame(win, state)
            
        elif state == states.GAME_ENDED: #When the game ends, prompt the user to save score
            state = saveScore(win, state, gameVariables)
            
        elif state == states.HIGH_SCORES:
            state = highScores(win, state)
            
        elif state == states.INST_MENU:
            state = instructionsMenu(win, state)
            
        #elif state == states.LEVEL_EDITOR:
            #state = levelEditor(win, state)
            
        elif state == states.CARACTER_SEL:
            state = caracterSelection(win, state)
            
        elif state == states.GAME_EXIT or win.closed:
            hasExited = True
            
        update(states.FPS)

def playGame(win, state):
    '''Draws the playing level, according to the current level number'''
    gameVariables = [1, 0, 0, 0, 0, 3, [], [], Text(Point(690, 715), ""), Image(Point(0,0), ""), Text(Point(700, 130), "Score"), Image(Point(0,0), ""), Image(Point(0,0), "")]
    drawLevel(win, gameVariables)
    l.drawHearts(win, gameVariables)
    l.drawScore(win, gameVariables)
    
    hasStarted = True
    isPlaying = False
    speed = 50
    ballSpeed = 5
    ballDir = -1
    goDown = 0
    times_moved = 0
    isPaused = False
    rocketActive = False
    
    '''Game Loop'''
    while hasStarted:
        key = win.checkKey()
        
        '''Pause Menu'''
        if isPaused:
            mouse = win.checkMouse()
            
        if not isPaused and key == 'Escape':
            pause = showPause(win)
            isPaused = True
        elif isPaused and (key == 'Escape' or resumeButton(mouse)):
            closePause(pause)
            isPaused = False
        elif isPaused and mainMenuButton(mouse):
            return states.MAIN_MENU, gameVariables
        
        if not isPaused:
            if isPlaying and goDown > states.FPS * var.time_sec and times_moved < gameVariables[var.level] * 10:
                goDown = 0
                moveBlocksDown(win, gameVariables)
                times_moved += 1
            
            '''Game hasnt started, waiting for player to start'''
            if key == 'space' and not isPlaying:
                isPlaying = True
                ballDir = startBall()
    
            '''Move player Paddle'''
            if key == 'Left' or key == 'Right':
                movePlayer(win, key, gameVariables[var.player], speed)
            
            '''Launch a rocket that destroys a set ammout of blocks'''
            if isPlaying and key == 'z' and not rocketActive and gameVariables[var.rockets] > 0:
                l.launchRocket(win, gameVariables)
                gameVariables[var.rockets] -= 1
                l.drawRockets(win, gameVariables)
                rocketActive = True
                
            if rocketActive:
                rocketActive = l.moveRocket(win, gameVariables)
            
            '''Move the paddle, while the game has not started'''
            if not isPlaying:
                if gameVariables[var.ball].getCenter().getX() != gameVariables[var.player].getAnchor().getX():
                    x = gameVariables[var.player].getAnchor().getX() - gameVariables[var.ball].getCenter().getX()
                    gameVariables[var.ball].move(x, 0)
                if gameVariables[var.ball].getCenter().getY() >= 750:
                    gameVariables[var.ball].move(0, -10)
            
            '''Detect collisions, ball movement, when die lose live and manage hearts'''
            if isPlaying and ballDir != -1:
                ballDir = checkCollisions(win, ballDir, gameVariables, var.ball_rad)
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
                times_moved = 0
                
            if gameVariables[var.level] > 3:
                hasStarted = False
        
            '''When all lives are lost, end the game'''
            if gameVariables[var.lives] <= 0:
                isPlaying = False
                hasStarted = False
        
            if isPlaying:
                goDown += 1
            
        update(states.FPS)
        
    return states.GAME_ENDED, gameVariables
    
def saveScore(win, state, gameVars):
    #Creates the file in case it does not exist
    text, tab, scoreText = promptUsername(win, gameVars[var.score])
    
    while win.checkKey() != 'Return':
        name = text.getText()
        
    name = name[:13]
    
    path = Path("scores.txt")
    
    if not path.is_file():
        file = open("scores.txt", "w")
        file.close()

    inFile = open("scores.txt", "r+")
    data = inFile.read()
    inFile.close()
    
    if "`" not in data:
        outFile = open("scores.txt", "w+")
        outFile.write(name + "´" + str(gameVars[var.score]) + "`")
        outFile.close()
    else:
        newData = scoresToList(data, name, gameVars[var.score])
        outFile = open("scores.txt", "w+")
        outFile.write(newData)
        outFile.close()
    
    scoreText.undraw()
    text.undraw()
    tab.undraw()
    
    return states.MAIN_MENU
    
def highScores(win, state):
    players, tab = drawHighscores(win)
    
    while win.getKey() != 'Escape':
        pass
    
    return states.MAIN_MENU

def instructionsMenu(win, state):
    tab = drawInstructions(win)
    
    while win.getKey() != 'Escape':
        pass
        
    tab.undraw()
        
    return states.MAIN_MENU
    
def caracterSelection(win, state):
    tab = drawDesign(win)
    dN, player = drawPlayerDesign(win)
    
    key = 'm'
    while key != 'Escape':
        key = win.checkKey()
        if key == 'Left':
            dN, player = minusDesign(dN, player, win) #dN = designNumber
        elif key == 'Right':
            dN, player = plusDesign(dN, player, win)
        
    saveDesign(dN)
    tab.undraw()
    player.undraw()
        
    return states.MAIN_MENU

main()