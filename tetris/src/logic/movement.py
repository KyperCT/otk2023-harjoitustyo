from model import tetris_block


def game_move(grid, blocks):
    if len(blocks) == 0:
        blocks.append(tetris_block.Block())
    for point in blocks[0]:
        grid.update(point[0], point[1], False)

    if not check_colisions(grid, blocks[0]):
        blocks[0].move_down()
    grid_update(grid, blocks)


def user_move(grid, keys, blocks):
    for point in blocks[0]:
        grid.update(point[0], point[1], False)

    if keys[0]:
        pass
    if keys[1]:
        if not check_left_colisions(grid, blocks[0]):
            blocks[0].move_left()
    if keys[2]:
        if not check_right_colisions(grid, blocks[0]):
            blocks[0].move_right()
    if keys[3]:
        if not check_colisions(grid, blocks[0]):
            blocks[0].move_down()
    grid_update(grid, blocks)


def grid_update(grid, blocks):
    if not check_colisions(grid, blocks[0]):
        for point in blocks[0]:
            grid.update(point[0], point[1], True)
    else:
        for point in blocks[0]:
            grid.update(point[0], point[1], True)
        blocks.pop()


def check_colisions(grid, block):
    for point in block:
        if point[1] == 19:
            return True
        elif grid.get(point[0], point[1]) or grid.get(point[0], point[1] + 1):
            return True
    return False


def check_left_colisions(grid, block):
    for point in block:
        if point[0] == 0:
            return True
        elif grid.get(point[0], point[1]) or grid.get(point[0] - 1, point[1]):
            return True
    return False


def check_right_colisions(grid, block):
    for point in block:
        if point[0] == 9:
            return True
        elif grid.get(point[0], point[1]) or grid.get(point[0] + 1, point[1]):
            return True
    return False
