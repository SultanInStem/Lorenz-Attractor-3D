import math 
import pygame
# import numpy as np 
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
            Vector((0,0,0),(100,0,0)),
            Vector((0,0,0), (0,100,0)),
            Vector((0,0,0), (0,0,100))
        ]

        self.angle = 3.14 / 2
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def update(self):
        for i in range(0, len(self.vectors)): 
            res = rotate_x(self.vectors[i].get_end_point(), self.angle)
            res = rotate_y(res, self.angle) 
            self.vectors[i].set_end_point(res)
        
    def render(self):
        self.screen.fill((0,0,0))

        for i in range(0, len(self.vectors)): 
            self.vectors[i].draw(self.screen)

        pygame.display.flip()
        self.clock.tick(30)
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()


