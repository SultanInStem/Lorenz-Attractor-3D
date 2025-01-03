import math 
import pygame
import sys
from globals import to_math_coords, to_screen_coords, rotate_x, rotate_y
from vector import Vector 



class Canvas: 
    def __init__(self, width, height): 
        pygame.init()
        pygame.display.set_caption("Lorenz Attactor 3D")
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen_size = self.screen.get_size()
        self.vectors = [
            Vector((0,0,0),(50,0,0)),
            Vector((0,0,0), (0,100,0)),
            Vector((0,0,0), (-30,0,100))
        ]

        self.angle = 0
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def update(self):
        pass
        
    def render(self):
        self.screen.fill((0,0,0))


        pygame.display.flip()
        self.clock.tick(60)
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()


