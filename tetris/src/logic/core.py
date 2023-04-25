from random import randint
from model import tetris_grid, tetris_block
from logic import movement, score


def core_loop(grid: tetris_grid.Grid, total_score: int, keys: tuple, state):
    if state is None:
        state = {"frame_value": 0, "blocks": [], "level": 1}

    if not state["blocks"]:
        total_score = score.check_score(grid, total_score)
        state["blocks"].append(tetris_block.Block(shape=(randint(0,6))))

    movement.user_move(grid, keys, state["blocks"])
    if state["frame_value"] == state["level"]*4:
        movement.game_move(grid, state["blocks"])
        state["frame_value"] = 0
    else:
        state["frame_value"] += 1

    return grid, total_score, state
