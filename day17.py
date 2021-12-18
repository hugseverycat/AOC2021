#target area: x=135..155, y=-102..-78
from math import sqrt

def step(pos, vel):
    vx, vy = vel
    x, y = pos
    
    y += vy
    vy -= 1
    
    x += vx
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
        
    return (x, y), (vx, vy)

def in_target(loc, x_tar, y_tar):
    x, y = loc

    xt1, xt2 = x_tar
    yt1, yt2 = y_tar
    
    if x in range(xt1, xt2 + 1) and y in range(yt1, yt2 + 1):
        return True
    return False
   

def estimate_x(x_tar):
    x_min, x_max = x_tar
    return round(sqrt(2 * x_min)), round(sqrt(2 * x_max))

x_target = (135, 155)
y_target = (-102, -78)

xmin, xmax = estimate_x(x_target)
max_y = 0

position = (0, 0)

'''for vx in range(xmin, xmax):
    this_max_y = 0
    hit_target = False
    vy = 1
    velocity = (vx, vy)
    while position[1] > y_target[1]:
        position, velocity = step(position, velocity)
        hit_target = in_target(position, x_target, y_target)
        if position[1] > this_max_y:
            
    if hit_target'''
    
velocity = (17, 101)   
i = 1
while position[1] > y_target[1]:
    position, velocity = step(position, velocity)
    print("step:", i, "position:", position, "velocity:", velocity)
    i += 1

