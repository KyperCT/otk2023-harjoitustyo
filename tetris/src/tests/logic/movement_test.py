import unittest
from unittest.mock import Mock, call
from model import tetris_block, tetris_grid
from logic import movement


class TestMovementFunctions(unittest.TestCase):
    def setUp(self):
        self.fake_block = Mock(tetris_block.Block(shape=0))
        self.fake_grid = Mock(tetris_grid.Grid())
        self.fake_grid.get = Mock(return_value=False)
        self.fake_block.__iter__ = Mock(
            return_value=iter([(0, 0), (0, 1), (1, 0), (1, 1)])
        )
    
    def test_check_floor_false_when_not_near_floor_and_no_grid_fill(self):
        check = movement.check_floor(self.fake_grid, self.fake_block)
        self.assertEqual(check, False)
    
    def test_check_floor_true_if_at_floor(self):
        self.fake_block.__iter__ = Mock(
            return_value=iter([(0, 18), (0, 19), (1, 18), (1, 19)])
        )
        check = movement.check_floor(self.fake_grid, self.fake_block)
        self.assertEqual(check, True)
    
    def test_check_floor_calls_block_iter(self):
        check = movement.check_floor(self.fake_grid, self.fake_block)
        self.fake_block.__iter__.assert_called()
    
    def test_check_floor_checks_correct_grid_points(self):
        check = movement.check_floor(self.fake_grid, self.fake_block)
        self.fake_grid.get.assert_has_calls(
            [call(0, 0), call(0, 1), call(1, 0), call(1, 1), 
             call(0, 1), call(0, 2), call(1, 1), call(1, 2)
            ], any_order=True)
    
    def test_check_floor_true_grid_fill(self):
        self.fake_grid.get = Mock(return_value=True)
        check = movement.check_floor(self.fake_grid, self.fake_block)
        self.assertEqual(check, True)
    
    def test_check_colisions_false_when_no_grid_fill(self):
        check = movement.check_colisions(self.fake_grid, self.fake_block)
        self.assertEqual(check, False)
    
    def test_check_colisions_calls_block_iter(self):
        check = movement.check_colisions(self.fake_grid, self.fake_block)
        self.fake_block.__iter__.assert_called()
    
    def test_check_colisions_checks_correct_grid_points(self):
        check = movement.check_colisions(self.fake_grid, self.fake_block)
        self.fake_grid.get.assert_has_calls(
            [call(0, 0), call(0, 1), call(1, 0), call(1, 1), 
            ], any_order=True)
    
    def test_check_colisions_true_grid_fill(self):
        self.fake_grid.get = Mock(return_value=True)
        check = movement.check_colisions(self.fake_grid, self.fake_block)
        self.assertEqual(check, True)

    def test_game_move_updates_block(self):
        movement.game_move(self.fake_grid, [self.fake_block])
        self.fake_block.move_down.assert_called_once()

    def test_game_move_clears_old_block(self):
        movement.game_move(self.fake_grid, [self.fake_block])
        self.fake_grid.update.assert_has_calls(
            [call(0, 0, False), call(0, 1, False), call(1, 0, False), call(1, 1, False)]
        )
