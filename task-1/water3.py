def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return True

def successors(s):
    x, y, z = s
    if x > 0:
        yield((0, y, z),x)
    if y > 0:
        yield((x, 0, z), y)
    if z > 0:
        yield((x, y, 0), z)
    if x < 4:
        yield((4, y, z), 4-x)
    if y < 4:
        yield((x, 4, z), 4-y)
    t = 4-x
    if y > 0 and t > 0:
        if x > t:
            yield((x-t, 4, z), t)
        else:
            yield((0, y+x, z), x)
    t = 4-y
    if x > 0 and t > 0:
        if x > t:
            yield((4, y-t, z), t)
        else:
            yield((x+y, 0, z), y)
    return []
