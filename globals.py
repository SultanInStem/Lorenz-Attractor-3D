def to_math_coords(point, screen_size): 
    math_x = point[0] - (screen_size[0] // 2)
    math_y = (screen_size[1] // 2) - point[1]

def to_screen_coords(point, screen_size): 
    pass 