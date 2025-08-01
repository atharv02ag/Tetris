import pygame

#time related
FPS = 60

#Block
CELL_SIZE = 40
COLUMNS = 10
ROWS = 20
TYPES = ['assets/Blue.png','assets/Red.png','assets/Yellow.png']

#game window
PADDING = CELL_SIZE/2
GAME_WIDTH = COLUMNS*CELL_SIZE
GAME_HEIGHT = ROWS*CELL_SIZE

#score window
SCORE_WIDTH = 4*CELL_SIZE
SCORE_HEIGHT = 4*CELL_SIZE

#screen window
SCREEN_HEIGHT = GAME_HEIGHT + 2*PADDING
SCREEN_WIDTH = GAME_WIDTH + SCORE_WIDTH + 3*PADDING

BACKGROUND_COLOR = (80,80,80) #gray
PANEL_COLOR = (0,0,0) #black

#tetromino shape
SPAWN_LOCATION = (4,1) #of top-left block
TETROMINO = {'T':[(-1,0),(0,-1),(0,0),(1,0)],
             'O':[(0,-1),(0,0),(1,-1),(1,0)],
             'J':[(0,-1),(1,-1),(1,0),(1,1)],
             'Z':[(0,-1),(1,-1),(1,0),(2,0)],
             'I':[(0,-2),(0,-1),(0,0),(0,1)],
             'L':[(0,-1),(0,0),(0,1),(1,1)],
             'S':[(0,-1),(1,-1),(0,0),(-1,0)]}

SHAPES = ['T','O','J','Z','I','L','S']
FALL_TIME = 800
MOVE_DETECT_TIME = 200

#Global variables

#OCCUPIED[y(row number)][x(column number)]
OCCUPIED = [[False for i in range(COLUMNS)] for j in range(ROWS)]