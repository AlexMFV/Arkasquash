from graphics import *

def promptUsername(win, score):
    tab = Image(Point(300, 400), "../resources/scoreSub.gif")
    tab.draw(win)
    score = Text(Point(398, 360), score)
    score.setSize(25)
    score.setTextColor("darkblue")
    score.setStyle("bold")
    score.draw(win)
    text = Entry(Point(398, 452), 10)
    text.setFace("arial")
    text.setStyle("bold")
    text.setSize(20)
    text.draw(win)
    return text, tab, score
    
def scoresToList(data, name, score):
    newData = data.split('`')
    names = []
    scores = []
    
    for i in newData:
        if i != '':
            names.append(i.split('´')[0])
            scores.append(i.split('´')[1])
            
    names.append(name)
    scores.append(str(score))
    
    #map, converts the list from string to int
    names, scores = sortLists(names, list(map(int, scores)))
    
    return convertListToString(names, scores)
    
def scoresToList2(data):
    newData = data.split('`')
    names = []
    scores = []
    
    for i in newData:
        if i != '':
            names.append(i.split('´')[0])
            scores.append(i.split('´')[1])
            
    return sortLists(names, list(map(int, scores)))
    
def sortLists(names, scores):
    for i in range(len(scores)):
       min = i
       for j in range(i+1, len(scores)):
           if scores[min] > scores[j]:
               min = j
       aux = scores[i]
       scores[i] = scores[min]
       scores[min] = aux
       aux2 = names[i]
       names[i] = names[min]
       names[min] = aux2
       
    if len(scores) > 10:
        value = (len(scores)-1) - 9
        for i in range(value-1, -1, -1):
            del scores[i]
            del names[i]
       
    return names, scores
    
def convertListToString(names, scores):
    newData = ""
    
    if len(scores) > 10:
        aux = 10
    else:
        aux = len(scores)
    
    for i in range(aux-1, -1, -1):
        newData += names[i] + "´" + str(scores[i]) + "`"
    
    return newData