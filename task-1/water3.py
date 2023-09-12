def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s == (4,4,0)

def successors(s):
    x, y, z = s
    if x > 0:
        yield((0, y, z),x)
    if y > 0:
        yield((x, 0, z),y)
    if z > 0:
        yield((x, y, 0),z)

    if x < 8:
        yield((8, y, z), 8-x)
    if y < 5:
        yield((x, 5, z), 5-y)
    if z < 3:
        yield((x, y, 3), 3-z)

    if x > 0 and y < 5:
        t = min(x, 5-y)
        yield((x-t, y+t, z), t)
    if x > 0 and z < 3:
        t = min(x, 3-z)
        yield((x-t, y, z+t), t)
    if y > 0 and x < 8:
        t =  min(y, 8-x)
        yield((x+t, y-t, z), t)
    if y > 0 and z < 3:
        t = min(y, 3-z)
        yield((x, y-t, z+t), t)
    if z > 0 and x < 8:
        t = min(z, 8-x)
        yield((x+t, y, z-t), t)
    if z > 0 and y < 5:
        t =  min(z, 5-y)
        yield((x, y+t, z-t), t)
