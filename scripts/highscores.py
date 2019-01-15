from graphics import *
from pathlib import *
from file import *

def drawHighscores(win):
    tab = Image(Point(400, 400), "../resources/highscores.gif")
    tab.draw(win)
    
    names = []
    scores = []
    
    path = Path("scores.txt")
    
    if not path.is_file():
        file = open("scores.txt", "w")
        file.close()

    inFile = open("scores.txt", "r+")
    data = inFile.read()
    inFile.close()
    
    names, scores = scoresToList2(data)
        
    if len(scores) < 10:
        scores = list(reversed(scores))
        names = list(reversed(names))
        value = 10 - len(scores)
        for i in range(value-1, -1, -1):
            scores.append(0)
            names.append("N/A")
    else:
        scores = list(reversed(scores))
        names = list(reversed(names))
    
    #First dashes and scores
    for i in range(10):
        if i >= 0 and i <= 2:
            text = Text(Point(300 , 300 + (55 * i)), "-")
            scoreT = Text(Point(380 , 300 + (55 * i)), scores[i])
        else:
            text = Text(Point(300 , 355 + (33 * i)), "-")
            scoreT = Text(Point(380 , 355 + (33 * i)), scores[i])
        text.setSize(25)
        scoreT.setSize(22)
        text.setStyle("bold")
        scoreT.setStyle("bold")
        if i == 0:
            text.setTextColor("gold")
            scoreT.setTextColor("gold")
        elif i == 1:
            text.setTextColor("silver")
            scoreT.setTextColor("silver")
        elif i == 2:
            text.setTextColor("sienna")
            scoreT.setTextColor("sienna")
        else:
            text.setTextColor("white")
            scoreT.setTextColor("white")
        text.draw(win)
        scoreT.draw(win)
    
    #Second dashes and 
    for i in range(10):
        if i >= 0 and i <= 2:
            text = Text(Point(460 , 300 + (55 * i)), "-")
            namesT = Text(Point(570 , 300 + (55 * i)), names[i])
        else:
            text = Text(Point(460 , 355 + (33 * i)), "-")
            namesT = Text(Point(570 , 355 + (33 * i)), names[i])
        text.setSize(25)
        namesT.setSize(20)
        text.setStyle("bold")
        namesT.setStyle("bold")
        if i == 0:
            text.setTextColor("gold")
            namesT.setTextColor("gold")
        elif i == 1:
            text.setTextColor("silver")
            namesT.setTextColor("silver")
        elif i == 2:
            text.setTextColor("sienna")
            namesT.setTextColor("sienna")
        else:
            text.setTextColor("white")
            namesT.setTextColor("white")
        text.draw(win)
        namesT.draw(win)
        
    return tab, text