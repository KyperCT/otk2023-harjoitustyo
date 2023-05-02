from model import tetris_block


def game_move(grid, blocks):
    """Excecutes block movement by the game

    Args:
      grid: tetris grid
      blocks: list of tetris blocks
    """
    for point in blocks[0]:
        grid.update(point[0], point[1], False)

    if not check_floor(grid, blocks[0]):
        blocks[0].move_down()
    grid_update(grid, blocks)


def user_move(grid, keys, blocks):
    """Excecutes block movement by the user

    Args:
      grid: tetris grid
      keys: keys pressed, tuple (up, left, right, down)
      blocks: list of tetris blocks
    """
    for point in blocks[0]:
        grid.update(point[0], point[1], False)

    if keys[0]:
        blocks[0].move_rotate()
        if check_colisions(grid, blocks[0]):
            blocks[0].unmove()
    if keys[1]:
        blocks[0].move_left()
        if check_colisions(grid, blocks[0]):
            blocks[0].unmove()
    if keys[2]:
        blocks[0].move_right()
        if check_colisions(grid, blocks[0]):
            blocks[0].unmove()
    if keys[3]:
        if not check_floor(grid, blocks[0]):
            blocks[0].move_down()
    grid_update(grid, blocks)


def grid_update(grid, blocks):
    """Updates grid with new block positions

    Args:
      grid: tetris grid
      blocks: list of tetris blocks
    """
    if not check_floor(grid, blocks[0]):
        for point in blocks[0]:
            grid.update(point[0], point[1], True)
    else:
        for point in blocks[0]:
            grid.update(point[0], point[1], True)
        blocks.pop()


def check_colisions(grid, block):
    """Checks if new block position conflicts with existing grid.

    Args:
      grid: tetris grid
      block: tetris block being checked

    Returns:
      True if there is a colision, False otherwise
    """
    for point in block:
        if grid.get(point[0], point[1]):
            return True
    return False


def check_floor(grid, block):
    """Checks if new block position conflicts with grid floor.

    Args:
      grid: tetris grid
      block: tetris block being checked

    Returns:
      True if there is a colision, False otherwise
    """
    for point in block:
        if point[1] == 19:
            return True
        if grid.get(point[0], point[1]) or grid.get(point[0], point[1] + 1):
            return True
    return False
