import pygame 
from globals import to_screen_coords, project_to_2d
class Vector: 
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos 
        self.end_pos = end_pos 
    def normalize(self): 
        pass 

    def draw(self, screen): 
        screen_size = screen.get_size()
        screen_start = project_to_2d(self.start_pos, 1)
        screen_end = project_to_2d(self.end_pos, 1)
        screen_start = to_screen_coords(screen_start, screen_size, 1)
        screen_end = to_screen_coords(screen_end, screen_size, 1)
        pygame.draw.line(screen, (255,255,255), screen_start, screen_end)     
    def get_end_point(self): 
        return self.end_pos 
    def set_end_point(self, point): 
        self.end_pos = point