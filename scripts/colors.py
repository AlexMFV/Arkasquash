import random as rand

colors = ["red", "green", "blue", "gold"]

def randomColor():
    value = rand.randint(0, 1000)
    if value >= 0 and value < 500:
        return colors[0]
    elif value >= 500 and value < 800:
        return colors[1]
    elif value >= 800 and value < 999:
        return colors[2]
    else:
        return colors[3]