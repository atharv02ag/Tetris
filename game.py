from settings import *
from random import randint
from tetromino import Tetromino
from timer import Timer
import globals
from collections import deque

class Game:
    def __init__(self):
        self.game_surface = pygame.Surface((GAME_WIDTH,GAME_HEIGHT))
        self.screen = pygame.display.get_surface()
        self.game_rect = self.game_surface.get_rect(topleft = (PADDING,PADDING))
        self.movement = ''
        self.movement_intensity = 0
        self.rows_to_be_adjusted = deque()
        
        #testing
        rand_shape = randint(0,6)
        rand_type = randint(0,2)

        self.sprites = pygame.sprite.Group()
        self.blocks_per_row = {}
        for row in range(ROWS):
            self.blocks_per_row[row] = pygame.sprite.Group()

        self.tetromino = Tetromino(self.sprites,SHAPES[rand_shape],rand_type)
        self.timers = {'FALL' : Timer(FALL_TIME,self.fall),
                       'GRAVITY' : Timer(GRAVITY_ADJUST_TIME, self.gravity_adjust_row)}

    def new_tetromino(self):
        rand_shape = randint(0,6)
        rand_type = randint(0,2)
        self.tetromino = Tetromino(self.sprites,SHAPES[rand_shape],rand_type)

    def fall(self):
        self.tetromino.fall()
    
    def gravity_adjust_row(self):
        if(len(self.rows_to_be_adjusted) == 0):
            return
        while(len(self.rows_to_be_adjusted) > 0):
            row_adjusted = self.rows_to_be_adjusted.pop()
            for row in range(row_adjusted-1,0,-1):
                for block in self.blocks_per_row[row]:
                    block.y += 1
                self.blocks_per_row[row+1] = self.blocks_per_row[row].copy()
                globals.OCCUPIED[row+1] = globals.OCCUPIED[row]
        
    def input(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT]):
            #print("left")
            self.movement = 'LEFT'
            self.movement_intensity += 1
        elif(keys[pygame.K_RIGHT]):
            #print("right")
            self.movement = 'RIGHT'
            self.movement_intensity += 1
        elif(keys[pygame.K_DOWN]):
            #print("down")
            self.movement = 'DOWN'
            self.movement_intensity += 1
        elif(keys[pygame.K_SPACE]):
            #print("rotate")
            self.movement = 'ROT'
            self.movement_intensity += 1
        else :
            self.movement = ''
            self.movement_intensity = 0

    def move(self):
        if(self.movement_intensity > 7):
            self.tetromino.shift(self.movement)
        elif(self.movement_intensity > 5):
            self.movement = ''
            self.movement_intensity = 0
        elif(self.movement_intensity > 4):
            self.tetromino.shift(self.movement)
    
    def occupy(self):
        for block in self.tetromino.blocks:
            globals.OCCUPIED[block.y][block.x] = True
            block.add(self.blocks_per_row[block.y])

    def clear_line(self):
        row = -1
        for i in range(ROWS):
            curr = i
            for j in range(COLUMNS):
                if(not globals.OCCUPIED[i][j]):
                    curr = -1
                    break
            if(curr != -1):
                row = curr
        if row == -1:
            return
        
        to_kill = []
        for block in self.sprites:
            if(block.y == row):
                to_kill.append(block)
                
        for col in range(COLUMNS):
            globals.OCCUPIED[row][col] = False

        for block in to_kill:
            pygame.sprite.Sprite.kill(block)

        self.rows_to_be_adjusted.append(row)
        globals.SCORE += 1

    def run(self):    
        self.screen.blit(self.game_surface,self.game_rect)
        self.game_surface.fill(PANEL_COLOR) #VERY IMPORTANT : TO FILL OVER (CLEAR) CONTENTS OF PREVIOUS FRAME

        self.input()
        self.clear_line()
        self.move()

        #if not falling, spawn new tetromino
        if(self.tetromino.next_move_vertical_collision(1)): 
            self.occupy()
            self.new_tetromino()
    
        self.timers['GRAVITY'].startTimer()
        self.timers['FALL'].startTimer()

        self.sprites.update()
        self.sprites.draw(self.game_surface)
