def initial_state():
    return (0, 0, 0)

def is_goal(s):
    return True

# returns a list of successors
def successors(s):

    # keeps track of bottle sizes
    bottle_size = [8, 5, 3]

    # note to self: pour until is empty or the other is full
    # first, get all possible combinations of pouring
    for from_index, from_amount in enumerate(s):
        for to_index, to_amount in enumerate(s):
            # make sure the bottle's not pouring into itself 
            if (from_index != to_index):
                # then, start pouring
                pour_amount = min(from_amount, bottle_size[to_index] - to_amount)
                if pour_amount != 0:
                    successor = list(s) # tuple doesn't allow assignments
                    successor[from_index] -= pour_amount
                    successor[to_index] += pour_amount
                    yield tuple(successor)


# just a little test for my successor
if __name__ == '__main__':
    print([i for i in successors((7, 4, 3))])
    # bottle max sizes are (8, 5, 3)
    # [(6, 5, 3), (8, 3, 3), (8, 4, 2), (7, 5, 2)] yayyy! it worrks