import unittest
from unittest.mock import Mock, call
from model import tetris_block, tetris_grid
from logic import movement


class TestMovementFunctions(unittest.TestCase):
    def setUp(self):
        self.fake_block = Mock(tetris_block.Block(shape=0))
        self.fake_grid = Mock(tetris_grid.Grid())
        self.fake_block.__iter__ = Mock(
            return_value=iter([(0, 0), (0, 1), (1, 0), (1, 1)])
        )

    def test_game_move_updates_block(self):
        movement.game_move(self.fake_grid, [self.fake_block])
        self.fake_block.move_down.assert_called_once()

    def test_game_move_clears_old_block(self):
        movement.game_move(self.fake_grid, [self.fake_block])
        self.fake_grid.update.assert_has_calls(
            [call(0, 0, False), call(0, 1, False), call(1, 0, False), call(1, 1, False)]
        )
