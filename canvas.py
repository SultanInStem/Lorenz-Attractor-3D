import math 
# import numpy as np
import pygame
import sys
from globals import to_math_coords, to_screen_coords
from vector import Vector 

t = 0

rotation_x = [
    [1,0,0], 
    [0, math.cos(t), -math.sin(t)], 
    [0, math.sin(t), math.cos(t)]
]

class Canvas: 
    def __init__(self, width, height): 
        pygame.init()
        pygame.display.set_caption("Lorenz Attactor 3D")
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen_size = self.screen.get_size()
        self.vector_x = Vector((0,0,0),(100,0,0))
        self.vector_y = Vector((0,0,0), (0,100,0))
        self.vector_z = Vector((0,0,0), (0,0,100))
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def update(self): 
        pass 

    def render(self):
        self.screen.fill((0,0,0))

        self.vector_x.draw(self.screen)
        self.vector_y.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(30)
    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()


