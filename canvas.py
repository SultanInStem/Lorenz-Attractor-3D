import pygame
import sys

class Canvas: 
    def __init__(self, width, height): 
        pygame.init()
        pygame.display.set_caption("Lorenz Attactor 3D")
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def update(self): 
        pass 

    def render(self):
        self.screen.fill((0,0,0))

        pygame.display.flip()
        self.clock.tick(30)
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()


