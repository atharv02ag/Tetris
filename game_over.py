from settings import *

class Game_Over:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.end_surface = pygame.Surface((GAME_WIDTH,GAME_HEIGHT))
        self.end_rect = self.end_surface.get_rect(topleft = (PADDING,PADDING))

    def run(self):
        pass