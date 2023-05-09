import unittest
from unittest.mock import Mock, call
from model import tetris_block, tetris_grid
from logic import core


class TestCoreFunctions(unittest.TestCase):
    def setUp(self):
        self.fake_block = Mock(tetris_block.Block(shape=0))
        self.fake_grid = Mock(tetris_grid.Grid())
        self.fake_grid.rows = 20
        self.keys = (False, False, False, False)
        self.state = {
            "frame_value": 0,
            "blocks": [self.fake_block],
            "level": 1,
            "fail": False,
        }
        self.fake_grid.get = Mock(return_value=False)

    def test_state_setup_correct_keys(self):
        grid, total_score, state = core.core_loop(self.fake_grid, 0, self.keys, None)
        self.assertEqual(state.keys(), self.state.keys())

    def test_state_setup_correct_values(self):
        grid, total_score, state = core.core_loop(self.fake_grid, 0, self.keys, None)
        state["blocks"] = type(state["blocks"][0])
        self.assertEqual(
            list(state.values()), [1, type(tetris_block.Block()), 1, False]
        )
