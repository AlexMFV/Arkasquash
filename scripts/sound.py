import winsound as sound
import threading

def playFreq(freq, time):
    sound.Beep(freq, time)
    
def playNextLevel(): #Done
    playFreq(600, 70)
    playFreq(600, 200)
    
def playDeath(): #Done
    playFreq(900, 50)
    playFreq(600, 50)
    playFreq(300, 100)
        
def playGetRocket(): #Done
    playFreq(300, 50)
    playFreq(600, 50)
    playFreq(900, 50)

def playBlockSound(): #Done
    playFreq(800, 50)
    
def playPaddleSound(): #Done
    playFreq(350, 50)
    
def playButton():
    playFreq(600, 100)