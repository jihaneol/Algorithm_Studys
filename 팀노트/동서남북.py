dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction,c):
    if c == "L":
        direction = (direction-1)%4
    else: direction = (direction+1)%4

    return direction

