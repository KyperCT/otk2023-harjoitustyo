from random import randint
from model import tetris_grid, tetris_block
from logic import movement, score


def core_loop(grid: tetris_grid.Grid, total_score: int, keys: tuple, state):
    """Core game loop, runs functions in order and tracks time

    Args:
      grid: tetris grid
      total_score: current score value
      keys: Keys pressed as tuple (up, left, right, down)
      state: dictionary which stores game state
    Returns:
      Tuple; tetris_grid object, total score and game state
    """
    if state is None:
        state = {"frame_value": 0, "blocks": [], "level": 1, "fail": False}

    if not state["blocks"]:
        total_score = score.check_score(grid, total_score)
        state["blocks"].append(tetris_block.Block(shape=randint(0, 6)))
        if movement.check_floor(grid, state["blocks"][0]):
            state["fail"] = True
            return grid, total_score, state
    movement.user_move(grid, keys, state["blocks"])
    if state["frame_value"] >= state["level"] * 4 and state["blocks"]:
        movement.game_move(grid, state["blocks"])
        state["frame_value"] = 0
    else:
        state["frame_value"] += 1

    return grid, total_score, state
