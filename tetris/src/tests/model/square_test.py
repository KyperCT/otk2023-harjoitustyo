import unittest
from model import tetris_block, tetris_grid


class TestBlockSquare(unittest.TestCase):
    def setUp(self):
        self.square = tetris_block.Block(shape=0)

    def test_square_is_square(self):
        self.assertEqual(
            tetris_block.Block(x_coord=0, y_coord=0, shape=0).block,
            [(0, 0), (0, 1), (1, 0), (1, 1)],
        )

    def test_square_default_placed_correctly(self):
        self.assertEqual(
            tetris_block.Block(shape=0).block, [(5, 0), (5, 1), (6, 0), (6, 1)]
        )

    def test_square_move_down(self):
        self.square.move_down()
        self.assertEqual(self.square.block, [(5, 1), (5, 2), (6, 1), (6, 2)])

    def test_square_move_left(self):
        self.square.move_left()
        self.assertEqual(self.square.block, [(4, 0), (4, 1), (5, 0), (5, 1)])

    def test_square_move_right(self):
        self.square.move_right()
        self.assertEqual(self.square.block, [(6, 0), (6, 1), (7, 0), (7, 1)])

    def test_square_down_no_oob(self):
        square = tetris_block.Block(x_coord=5, y_coord=18, shape=0)
        self.assertEqual(square.block, [(5, 18), (5, 19), (6, 18), (6, 19)])
        square.move_down()
        self.assertEqual(square.block, [(5, 18), (5, 19), (6, 18), (6, 19)])

    def test_square_left_no_oob(self):
        square = tetris_block.Block(x_coord=0, y_coord=0, shape=0)
        self.assertEqual(square.block, [(0, 0), (0, 1), (1, 0), (1, 1)])
        square.move_left()
        self.assertEqual(square.block, [(0, 0), (0, 1), (1, 0), (1, 1)])

    def test_square_right_no_oob(self):
        square = tetris_block.Block(x_coord=8, y_coord=0, shape=0)
        self.assertEqual(square.block, [(8, 0), (8, 1), (9, 0), (9, 1)])
        square.move_right()
        self.assertEqual(square.block, [(8, 0), (8, 1), (9, 0), (9, 1)])

    def test_iterator_returns_points(self):
        output = []
        for point in self.square:
            output.append(point)
        self.assertEqual(output, [(5, 0), (5, 1), (6, 0), (6, 1)])
