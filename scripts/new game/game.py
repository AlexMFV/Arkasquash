ball_dir = ["LU", "RU", "RD", "LD"]

def movePlayer(win, key, player, speed):
    if key == 'Left' and player.getAnchor().getX() > 50:
        player.move(-speed, 0)
    if key == 'Right' and player.getAnchor().getX() < 550:
        player.move(speed, 0)
        
def startBall():
    
def moveBall():
    pass
    
def checkCollisions():
    pass