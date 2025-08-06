from settings import COLUMNS, ROWS

#OCCUPIED[y(row number)][x(column number)]
OCCUPIED = [[False for i in range(COLUMNS)] for j in range(ROWS)]
SCORE = 0
LINES = 0
GAME_OVER = False