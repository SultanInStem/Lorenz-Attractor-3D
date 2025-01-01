import math
import numpy as np 
def to_math_coords(point, screen_size): 
    math_x = point[0] - (screen_size[0] // 2)
    math_y = (screen_size[1] // 2) - point[1]
    return (math_x, math_y)

def to_screen_coords(point, screen_size, scale): 
    screen_x = point[0] * scale + (screen_size[0] // 2)
    screen_y = (screen_size[1] // 2) - point[1] * scale
    return (screen_x, screen_y)

def project_to_2d(point, focal_length): 
    x,y,z = point 
    if z == - focal_length:
        z += 1e-6 
    x_proj = focal_length * x / (focal_length + z)
    y_proj = focal_length * y / (focal_length + z)
    return (x_proj, y_proj)


def rotate_x(point, angle): 
    A = [
        [1,0,0], 
        [0, math.cos(angle), -math.sin(angle)], 
        [0, math.sin(angle), math.cos(angle)]
    ]
    V = [point[0], point[1], point[2]]
    res = np.matmul(A, V)
    return (res[0], res[1], res[2]) 

def rotate_y(point, angle): 
    A = [ 
        [math.cos(angle), 0, math.sin(angle)], 
        [0,1,0], 
        [-math.sin(angle), 0, math.cos(angle)]
    ]
    V = [point[0], point[1], point[2]]
    res = np.matmul(A, V)
    return (res[0], res[1], res[2]) 
