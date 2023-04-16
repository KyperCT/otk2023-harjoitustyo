import unittest
from model import tetris_block, tetris_grid


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = tetris_grid.Grid()

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

    def test_empty_row_check_false(self):
        self.assertEqual(self.grid.check_row(1), False)
    
    def test_partial_row_check_false(self):
        self.grid.update(0, 1, True)
        self.grid.update(0, 3, True)
        self.grid.update(0, 5, True)
        self.assertEqual(self.grid.check_row(1), False)
    
    def test_full_row_check_true(self):
        for i in range(0,10):
            self.grid.update(i, 1, True)
        self.assertEqual(self.grid.check_row(1), True)

    #Add tests for shift_down_over

class TestBlockSquare(unittest.TestCase):
    def setUp(self):
        self.square = tetris_block.Block(shape=0)
    
    def test_square_is_square(self):
        self.assertEqual(tetris_block.Block(x_coord=0,y_coord=0,shape=0).block, 
                        [(0, 0), (0, 1), (1, 0), (1, 1)])

    def test_square_default_placed_correctly(self):
        self.assertEqual(tetris_block.Block(shape=0).block, 
                        [(5, 0), (5, 1), (6, 0), (6, 1)])
    
    def test_square_move_down(self):
        self.square.move_down()
        self.assertEqual(self.square.block, 
                        [(5, 1), (5, 2), (6, 1), (6, 2)])
    
    def test_square_move_left(self):
        self.square.move_left()
        self.assertEqual(self.square.block, 
                        [(4, 0), (4, 1), (5, 0), (5, 1)])
    
    def test_square_move_right(self):
        self.square.move_right()
        self.assertEqual(self.square.block, 
                        [(6, 0), (6, 1), (7, 0), (7, 1)])
    
    def test_square_down_no_oob(self):
        square = tetris_block.Block(x_coord=5,y_coord=18,shape=0)
        self.assertEqual(square.block,
                        [(5, 18), (5, 19), (6, 18), (6, 19)])
        square.move_down()
        self.assertEqual(square.block,
                        [(5, 18), (5, 19), (6, 18), (6, 19)])
    
    def test_square_left_no_oob(self):
        square = tetris_block.Block(x_coord=0,y_coord=0,shape=0)
        self.assertEqual(square.block,
                        [(0, 0), (0, 1), (1, 0), (1, 1)])
        square.move_left()
        self.assertEqual(square.block,
                        [(0, 0), (0, 1), (1, 0), (1, 1)])
    
    def test_square_right_no_oob(self):
        square = tetris_block.Block(x_coord=8,y_coord=0,shape=0)
        self.assertEqual(square.block,
                        [(8, 0), (8, 1), (9, 0), (9, 1)])
        square.move_right()
        self.assertEqual(square.block,
                        [(8, 0), (8, 1), (9, 0), (9, 1)])
    
    def test_iterator_returns_points(self):
        output = []
        for point in self.square:
            output.append(point)
        self.assertEqual(output, [(5, 0), (5, 1), (6, 0), (6, 1)])