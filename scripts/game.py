from random import *
import common as var
import blocks as bs
from graphics import *

def movePlayer(win, key, player, speed):
    if key == 'Left' and player.getAnchor().getX() > 50:
        player.move(-speed, 0)
    if key == 'Right' and player.getAnchor().getX() < 550:
        player.move(speed, 0)
        
def startBall():
    return randint(0, 1)

def checkCollisions(win, dir, gameVariables, rad):
    d = ["LU", "RU", "RD", "LD"]
    
    ballX = gameVariables[var.ball].getCenter().getX()
    ballY = gameVariables[var.ball].getCenter().getY()
    
    playerX = gameVariables[var.player].getAnchor().getX()
    playerY = gameVariables[var.player].getAnchor().getY()
    
    '''Collisions with the boundaries of the play area'''
    if d[dir] == "LU" and ballX - rad <= 0:
        dir = changeDirection('+', dir)
    
    if d[dir] == "LU" and ballY - rad <= 0:
        dir = changeDirection('-', dir)
        
    if d[dir] == "RU" and ballX + rad >= 600:
        dir = changeDirection('-', dir)
    
    if d[dir] == "RU" and ballY - rad <= 0:
        dir = changeDirection('+', dir)
        
    if d[dir] == "RD" and ballX + rad >= 600:
        dir = changeDirection('+', dir)
    
    if d[dir] == "RD" and ballY + rad >= 790:
        return -1
        
    if d[dir] == "LD" and ballX - rad <= 0:
        dir = changeDirection('-', dir)
    
    if d[dir] == "LD" and ballY + rad >= 790:
        return -1
        
    '''Collisions with the paddle'''
    if d[dir] == "RD":
        if ballY + rad >= playerY - (var.playerHeight /2) and ballY + rad <= playerY + (var.playerHeight /2):
            if ballX + rad >= playerX - (var.playerLength /2) and ballX + rad <= playerX + (var.playerLength /2):
                dir = changeDirection('-', dir)
        
    if d[dir] == "LD":
        if ballY + rad >= playerY - (var.playerHeight /2) and ballY + rad <= playerY + (var.playerHeight /2):
            if ballX + rad >= playerX - (var.playerLength /2) and ballX + rad <= playerX + (var.playerLength /2):
                dir = changeDirection('+', dir)
    
    '''Collisions with individual blocks'''
    aux = 0
    for b in gameVariables[var.blocks]:
        if d[dir] == "LU" or d[dir] == "LD":
            bX = b.getP2().getX()
            bY = b.getP2().getY()
        else:
            bX = b.getP1().getX()
            bY = b.getP1().getY()
        
        if d[dir] == "LU": #DONE
            if ballX <= bX and ballX >= bX - var.block_width:
                if ballY - rad <= bY and ballY - rad >= bY - rad:
                    dir = changeDirection('-', dir)
                    bs.addPoints(win, aux, gameVariables)
                    bs.removeBlock(aux, gameVariables)
                    break
            if ballX - rad <= bX and ballX - rad >= bX - rad:
                if ballY <= bY and ballY >= bY - var.block_height:
                    dir = changeDirection('+', dir)
                    bs.addPoints(win, aux, gameVariables)
                    bs.removeBlock(aux, gameVariables)
                    break
            
        if d[dir] == "RU": #DONE
            if ballX >= bX and ballX <= bX + var.block_width:
                if ballY - rad <= bY + var.block_height and ballY - rad >= (bY + var.block_height) - rad:
                    dir = changeDirection('+', dir)
                    bs.addPoints(win, aux, gameVariables)
                    bs.removeBlock(aux, gameVariables)
                    break
            if ballX + rad >= bX and ballX + rad <= bX + rad:
                if ballY >= bY and ballY <= bY + var.block_height:
                    dir = changeDirection('-', dir)
                    bs.addPoints(win, aux, gameVariables)
                    bs.removeBlock(aux, gameVariables)
                    break
            
        if d[dir] == "RD": #DONE
            if ballX >= bX and ballX <= bX + var.block_width:
                if ballY + rad >= bY and ballY + rad <= bY + rad:
                    dir = changeDirection('-', dir)
                    bs.addPoints(win, aux, gameVariables)
                    bs.removeBlock(aux, gameVariables)
                    break
            if ballX + rad >= bX and ballX + rad <= bX + rad:
                if ballY >= bY and ballY <= bY + var.block_height:
                    dir = changeDirection('+', dir)
                    bs.addPoints(win, aux, gameVariables)
                    bs.removeBlock(aux, gameVariables)
                    break
            
        if d[dir] == "LD": #DONE
            if ballX <= bX and ballX >= (bX - var.block_width):
                if ballY + rad >= bY - var.block_height and ballY + rad <= (bY - var.block_height) + rad:
                    dir = changeDirection('+', dir)
                    bs.addPoints(win, aux, gameVariables)
                    bs.removeBlock(aux, gameVariables)
                    break
            if ballX - rad <= bX and ballX - rad >= bX - rad:
                if ballY <= bY and ballY >= bY - var.block_height:
                    dir = changeDirection('-', dir)
                    bs.addPoints(win, aux, gameVariables)
                    bs.removeBlock(aux, gameVariables)
                    break
            
        aux += 1
        
    return dir
        
def changeDirection(rate, dir):
    if rate == '-':
        dir -= 1
    else:
        dir += 1
    
    if dir < 0:
        return 3
    
    if dir > 3:
        return 0
        
    return dir
        
def moveBall(dir, speed, gameVariables):
    directions = ["LU", "RU", "RD", "LD"]
    
    if directions[dir] == "LU":
        gameVariables[var.ball].move(-speed, -speed)
        
    if directions[dir] == "RU":
        gameVariables[var.ball].move(speed, -speed)
        
    if directions[dir] == "RD":
        gameVariables[var.ball].move(speed, speed)
        
    if directions[dir] == "LD":
        gameVariables[var.ball].move(-speed, speed)
        
def showPause(win):
    menu = Image(Point(300, 400), "../resources/pause_menu.gif")
    menu.draw(win)
    return menu
    
def closePause(menu):
    menu.undraw()
    
def resumeButton(mouse):
    if mouse != None:
        if mouse.getX() >= 196 and mouse.getX() <= 396:
            if mouse.getY() >= 390 and mouse.getY() <= 450:
                return True
            else:
                return False
        else:
            return False
        
def mainMenuButton(mouse):
    if mouse != None:
        if mouse.getX() >= 196 and mouse.getX() <= 396:
            if mouse.getY() >= 470 and mouse.getY() <= 525:
                return True
            else:
                return False
        else:
            return False
    