from settings import *

class Block(pygame.sprite.Sprite):

#sprites MUST have two attributes - self.rect for positioning and self.image as the surface to be drawn
#type can take 3 values 
    def __init__(self,pos,group,type): 
        super().__init__(group) #adds self to sprite group 
        self.image = pygame.image.load(TYPES[type]).convert_alpha()
        self.x = pos[0] #column number
        self.y = pos[1] #row number
        self.rect = self.image.get_rect(topleft = (self.x*CELL_SIZE, self.y*CELL_SIZE))
        self.falling = True
        self.gravity = False

    def update(self):
        self.rect.topleft = (self.x*CELL_SIZE, self.y*CELL_SIZE)

    def will_horizontal_collide(self,x_pos):
        if(x_pos>=0 and x_pos<COLUMNS and not OCCUPIED[self.y][x_pos]):
            return False
        else:
            return True
        
    def will_vertical_collide(self,y_pos):
        if(y_pos<ROWS and not OCCUPIED[y_pos][self.x]):
            return False
        else:
            return True