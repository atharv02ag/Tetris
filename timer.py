from pygame.time import get_ticks

class Timer:
    def __init__(self, duration,func=None): #duration is in ms
        self.start_time = 0
        self.duration = duration
        self.func = func
        self.active = False

    def activate(self):
        self.start_time = get_ticks()
        self.active = True

    def reset(self):
        self.start_time = 0
        self.active = False
    
    def startTimer(self):
        if(not self.active):
            self.activate()
        current_time = get_ticks()
        if((current_time-self.start_time)>=self.duration):
            if(self.func):
                self.func()
            self.reset()
