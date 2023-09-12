def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s == (4, 4, 0)

def successors(s):
    x, y, z = s # x = 8-liter, y = 5-liter, z = 3-liter
    successors_list = []

    # 8-liter bottle to 5-liter bottle
    if x > 0 and y < 5:
        amount_poured = min(x, 5 - y)
        new_state = (x - amount_poured, y + amount_poured, z)
        successors_list.append((new_state, amount_poured))

    # 8-liter bottle to 3-liter bottle
    if x > 0 and z < 3:
        amount_poured = min(x, 3 - z)
        new_state = (x - amount_poured, y, z + amount_poured)
        successors_list.append((new_state, amount_poured))

    # 5-liter bottle to 8-liter bottle
    if y > 0 and x < 8:
        amount_poured = min(y, 8 - x)
        new_state = (x + amount_poured, y - amount_poured, z)
        successors_list.append((new_state, amount_poured))

    # 5-liter bottle to 3-liter bottle
    if y > 0 and z < 3:
        amount_poured = min(y, 3 - z)
        new_state = (x, y - amount_poured, z + amount_poured)
        successors_list.append((new_state, amount_poured))

    # 3-liter bottle to 8-liter bottle
    if z > 0 and x < 8:
        amount_poured = min(z, 8 - x)
        new_state = (x + amount_poured, y, z - amount_poured)
        successors_list.append((new_state, amount_poured))

    # Pour from 3-liter bottle to 5-liter bottle
    if z > 0 and y < 5:
        amount_poured = min(z, 5 - y)
        new_state = (x, y + amount_poured, z - amount_poured)
        successors_list.append((new_state, amount_poured))

    return successors_list
