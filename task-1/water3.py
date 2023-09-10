def initial_state():
    return (0, 0, 0)

def is_goal(s):
    return S[0] ==4 and S[1] == 4

def successors(s):
    x, y, z = s
    return []
