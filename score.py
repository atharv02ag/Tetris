from settings import *
import globals

class Score:
    def __init__(self):

        self.screen = pygame.display.get_surface()
        self.score_surface = pygame.Surface((SCORE_WIDTH,SCORE_HEIGHT))
        self.score_rect = self.score_surface.get_rect(topleft=(2*PADDING + GAME_WIDTH, PADDING))
        pygame.font.init()
        self.score_font = pygame.font.SysFont('Serif',30)

    def run(self):

        self.screen.blit(self.score_surface,self.score_rect)
        self.score_surface.fill(PANEL_COLOR)
        self.score_text = self.score_font.render(f"Score : {globals.SCORE}", False, (255,255,255))
        self.score_text_rect = self.score_text.get_rect(topleft = (PADDING/2 ,PADDING/2))
        self.score_surface.blit(self.score_text, self.score_text_rect)
        print("score run ", globals.SCORE)
