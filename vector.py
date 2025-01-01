import pygame 
from globals import to_screen_coords, project_to_2d
class Vector: 
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos 
        self.end_pos = end_pos 
    def normalize(self): 
        pass 

    def draw(self, screen): 
        pass
    def get_end_point(self): 
        return self.end_pos 
    def set_end_point(self, point): 
        self.end_pos = point