import pygame 
import numpy as np 
from globals import to_screen_coords
class Vector: 
    def __init__(self, start_pos, end_pos):
        self.start_pos = np.array(start_pos) 
        self.end_pos = np.array(end_pos) 
    def normalize(self): 
        pass 

    def draw(self, screen): 
        pass
