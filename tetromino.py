from settings import *
from block import Block
               
class Tetromino:
    #shape - L,J,O etc. while type = 0,1,2 indicating colour
    def __init__(self,group,shape,type):
        self.shape = shape
        self.block_positions = TETROMINO[self.shape]

        #blocks making up the tetromino
        self.blocks = [Block((SPAWN_LOCATION[0]+position[0],SPAWN_LOCATION[1]+position[1]),group,type) for position in self.block_positions]

    def fall(self):
        if(not self.next_move_vertical_collision(1)):
            for block in self.blocks:
                block.y += 1

    def shift(self,direction:str):
        if(direction == 'LEFT' and not self.next_move_horizontal_collision(-1) and not self.next_move_vertical_collision(1)):
            for block in self.blocks:
                block.x += -1
        elif (direction == 'RIGHT' and not self.next_move_horizontal_collision(1) and not self.next_move_vertical_collision(1)):
            for block in self.blocks:
                block.x += 1  
        elif (direction == 'ROT' and not self.next_move_rotation_collision):
            self.rotate() #to write
    
    def rotate(self): #to write
        pass
    
    def next_move_horizontal_collision(self,amount): #amount can be 1 or -1
        next_positions = [block.will_horizontal_collide(block.x+amount) for block in self.blocks]
        result = False
        for pos in next_positions:
            if(pos):
                result = True
                break
        return result

    def next_move_vertical_collision(self,amount):
        next_positions = [block.will_vertical_collide(block.y+amount) for block in self.blocks]
        result = False
        for pos in next_positions:
            if(pos):
                result = True
                break
        return result
    
    def next_move_rotation_collision(self): 
        next_positions = [block.will_rotate_collide() for block in self.blocks]
        result = False
        for pos in next_positions:
            if(pos):
                result = True
                break
        return result