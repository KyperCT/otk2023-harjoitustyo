import unittest
from logic import movement

class FakeBlock:
    def __init__(self, x=None, y=None, shape=0):
        self.block_down_move_count = 0
        self.block_left_move_count = 0
        self.block_right_move_count = 0
    
    def move_down(self):
        self.block_down_move_count += 1
    
    def move_left(self):
        self.block_left_move_count += 1
    
    def move_right(self):
        self.block_right_move_count += 1
    
    def __iter__(self):
        return (point for point in [(5,0),(6,0),(5,1),(6,1)])


class TestMovementFunctions(unittest.TestCase):
    def setUp(self):
        self.fake_blocks = [FakeBlock()]
    
    def test_game_move_updates_block(self):
        movement.game_move(self.grid, self.fake_blocks)
        self.assertEqual(self.fake_blocks[0].block_down_move_count, 1)