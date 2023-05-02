import unittest
from unittest.mock import Mock, call
from model import tetris_block, tetris_grid
from logic import score


class TestScoreFunctions(unittest.TestCase):
    def setUp(self):
        self.fake_block = Mock(tetris_block.Block(shape=0))
        self.fake_grid = Mock(tetris_grid.Grid())
        self.fake_grid.rows = 20
        self.score = 123
        self.grid_effects = {x: False for x in range(0, 20)}
        self.fake_grid.check_row.side_effect = lambda x: self.grid_effects[x] 

    def test_check_score_checks_all_rows(self):
        new_score = score.check_score(self.fake_grid, self.score)
        self.fake_grid.check_row.assert_has_calls([call(x) for x in range(0,20)], any_order=True)

    def test_check_score_doesnt_change_when_no_full_rows(self):
        new_score = score.check_score(self.fake_grid, self.score)
        self.assertEqual(new_score, self.score)
    
    def test_check_score_grows_by_200_one_clear(self):
        self.grid_effects[19] = True
        new_score = score.check_score(self.fake_grid, self.score)
        self.assertEqual(new_score, 200+self.score)

    def test_check_score_grows_by_400_two_clears(self):
        self.grid_effects[19] = True
        self.grid_effects[18] = True
        new_score = score.check_score(self.fake_grid, self.score)
        self.assertEqual(new_score, 400+self.score)

    def test_check_score_grows_by_800_three_clears(self):
        self.grid_effects[19] = True
        self.grid_effects[18] = True
        self.grid_effects[17] = True
        new_score = score.check_score(self.fake_grid, self.score)
        self.assertEqual(new_score, 800+self.score)
    
    def test_check_score_grows_by_1600_four_clears(self):
        self.grid_effects[19] = True
        self.grid_effects[18] = True
        self.grid_effects[17] = True
        self.grid_effects[16] = True
        new_score = score.check_score(self.fake_grid, self.score)
        self.assertEqual(new_score, 1600+self.score)

    def test_check_score_doesnt_call_shift_down_no_clears(self):
        new_score = score.check_score(self.fake_grid, self.score)
        self.fake_grid.shift_down_over.assert_not_called()
    
    def test_check_score_calls_shift_down_once_one_clear(self):
        self.grid_effects[19] = True
        new_score = score.check_score(self.fake_grid, self.score)
        self.fake_grid.shift_down_over.assert_called_once()

    def test_check_score_calls_shift_down_twice_two_clears(self):
        self.grid_effects[19] = True
        self.grid_effects[18] = True
        new_score = score.check_score(self.fake_grid, self.score)
        self.assertEqual(self.fake_grid.shift_down_over.call_count, 2)

    def test_check_score_calls_shift_down_thrice_three_clears(self):
        self.grid_effects[19] = True
        self.grid_effects[18] = True
        self.grid_effects[17] = True
        new_score = score.check_score(self.fake_grid, self.score)
        self.assertEqual(self.fake_grid.shift_down_over.call_count, 3)
    
    def test_check_score_calls_shift_down_4_times_4_clears(self):
        self.grid_effects[19] = True
        self.grid_effects[18] = True
        self.grid_effects[17] = True
        self.grid_effects[16] = True
        new_score = score.check_score(self.fake_grid, self.score)
        self.assertEqual(self.fake_grid.shift_down_over.call_count, 4)