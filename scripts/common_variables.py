from graphics import *

'''0 - Level Editor / 1,2,3 - Normal Levels'''
level_num = 3

'''Score, Powers, Extras and Lives'''
score = 0
power_rocket = 0
power_lazer = 0
extra_ball = 0
lives = 3

'''Play Area Variables'''
top_offset = 50
side_offset = 25
block_width = 55
block_height = 20
blocks = []
block_colors = []
block_outline = 1
outlineColor = "white"

'''Strings for Scores, Lives, Extras and Powers'''
hearts = ["one", "two", "three"]
livesText = Text(Point(690, 715), "")
livesImage = 0