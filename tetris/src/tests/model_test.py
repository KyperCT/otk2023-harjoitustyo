import unittest
from model import tetris_block, tetris_grid


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = tetris_grid.Grid()
        self.square = tetris_block.Block(shape=0)

    def test_grid_starts_empty(self):
        is_not_empty = False
        for point in self.grid:
            if point[0]:
                is_not_empty = True
        self.assertEqual(is_not_empty, False)
    
    def test_update_grid_can_fill_points(self):
        self.grid.update(0, 5, True)
        is_not_empty = False
        for point in self.grid:
            if point[0]:
                is_not_empty = True
        self.assertEqual(is_not_empty, True)
    
    def test_update_grid_can_clear_points(self):
        self.grid.update(0, 5, True)
        self.grid.update(0, 5, False)
        is_not_empty = False
        for point in self.grid:
            if point[0]:
                is_not_empty = True
        self.assertEqual(is_not_empty, False)
    
    def test_get_grid_gets_points(self):
        output = []
        self.grid.update(4, 5, True)
        self.grid.update(7, 12, True)
        self.grid.update(1, 15, True)
        output.append(self.grid.get(4, 5))
        output.append(self.grid.get(6, 6))
        output.append(self.grid.get(7, 10))
        output.append(self.grid.get(7, 12))
        output.append(self.grid.get(0, 15))
        output.append(self.grid.get(1, 15))
        self.assertEqual(output, [True, False, False, True, False, True])
