from settings import *
from random import randint
from block import Block
from tetromino import Tetromino
from timer import Timer

class Game:
    def __init__(self):
        self.game_surface = pygame.Surface((GAME_WIDTH,GAME_HEIGHT))
        self.screen = pygame.display.get_surface()
        self.game_rect = self.game_surface.get_rect(topleft = (PADDING,PADDING))
        self.movement = ''
        
        #testing
        shapes = ['T','O','J','Z','I','L','S']
        rand_shape = randint(0,6)
        rand_type = randint(0,2)

        self.sprites = pygame.sprite.Group()
        self.tetromino = Tetromino(self.sprites,shapes[rand_shape],rand_type)
        self.timers = {'FALL' : Timer(FALL_TIME,self.fall),
                       'MOTION' : Timer(MOVE_DETECT_TIME,self.move)}

    def new_tetromino(self):
        shapes = ['T','O','J','Z','I','L','S']
        rand_shape = randint(0,6)
        rand_type = randint(0,2)
        self.tetromino = Tetromino(self.sprites,shapes[rand_shape],rand_type)

    def fall(self):
        self.tetromino.fall()

    def input(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT]):
            self.movement = 'LEFT'
        elif(keys[pygame.K_RIGHT]):
            self.movement = 'RIGHT'
        elif(keys[pygame.K_DOWN]):
            self.movement = 'DOWN'
        elif(keys[pygame.K_SPACE]):
            print('i am rotaty boy')
            self.movement = 'ROT'

    def move(self):
        self.tetromino.shift(self.movement)
        if(not self.movement == 'DOWN'):
            self.movement = ''
    
    def occupy(self):
        global OCCUPIED
        for block in self.tetromino.blocks:
            OCCUPIED[block.y][block.x] = True

    def clear_line(self):
        global OCCUPIED
        row = -1
        for i in range(ROWS):
            curr = i
            for j in range(COLUMNS):
                if(not OCCUPIED[i][j]):
                    curr = -1
                    break
            row = curr
            if(row != -1):
                break
        #print(row) #finds filled row

    def run(self):    
        self.screen.blit(self.game_surface,self.game_rect)
        self.game_surface.fill(PANEL_COLOR) #VERY IMPORTANT : TO FILL OVER (CLEAR) CONTENTS OF PREVIOUS FRAME

        #if not falling, spawn new tetromino
        if(self.tetromino.next_move_vertical_collision(1)): 
            self.occupy()
            self.new_tetromino()

        self.input()
        if(self.movement == 'DOWN'):
            self.timers['FALL'].duration = MOVE_DETECT_TIME
            self.movement = ''
        else :
            self.timers['FALL'].duration = FALL_TIME

        self.clear_line()
    
        self.timers['MOTION'].startTimer()
        self.timers['FALL'].startTimer()
        self.sprites.update()
        self.sprites.draw(self.game_surface)
