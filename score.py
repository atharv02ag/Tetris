from settings import *
import globals

class Score:
    def __init__(self):

        self.screen = pygame.display.get_surface()
        self.score_surface = pygame.Surface((SCORE_WIDTH,SCORE_HEIGHT))
        self.score_rect = self.score_surface.get_rect(topleft=(2*PADDING + GAME_WIDTH, PADDING))
        pygame.font.init()
        self.font = pygame.font.SysFont('Serif',30)

    def run(self):

        self.screen.blit(self.score_surface,self.score_rect)
        self.score_surface.fill(PANEL_COLOR)
        self.score_text = self.font.render(f"Score : {globals.SCORE}", False, SCORE_FONT_COLOR)
        self.score_text_rect = self.score_text.get_rect(topleft = (PADDING/2 ,PADDING/2))
        self.line_text = self.font.render(f"Lines : {globals.LINES}", False, SCORE_FONT_COLOR)
        self.line_text_rect = self.line_text.get_rect(topleft = (PADDING/2, 2*PADDING))
        self.score_surface.blit(self.score_text, self.score_text_rect)
        self.score_surface.blit(self.line_text, self.line_text_rect)
