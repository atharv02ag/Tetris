from sys import exit
from settings import *
from game import Game
from score import Score

class Main() :
    def __init__(self):

        #setup  
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()

        #components
        self.game = Game()
        self.score = Score()

    def run(self):
        running = True

        #game loop
        while running :
            #event handler
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
                    pygame.quit()
                    exit()

            #to clear contents of previous frame
            self.screen.fill(BACKGROUND_COLOR)

            #running components
            self.score.run()       
            self.game.run()

            #screen update
            pygame.display.update()
            self.clock.tick(FPS)

#https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if(__name__ == '__main__'):
    main = Main()
    main.run()
    