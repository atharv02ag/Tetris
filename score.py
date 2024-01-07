from settings import *

class Score:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.score_surface = pygame.Surface((SCORE_WIDTH,SCORE_HEIGHT))
        self.score_rect = self.score_surface.get_rect(topleft=(2*PADDING + GAME_WIDTH, PADDING))

    def run(self):
        self.screen.blit(self.score_surface,self.score_rect)
