import unittest
from model import tetris_block, tetris_grid


class TestBlockLine(unittest.TestCase):
    def setUp(self):
        self.line = tetris_block.Block(shape=1)

    def test_line_is_line(self):
        self.assertEqual(
            tetris_block.Block(x_coord=0, y_coord=0, shape=1).block,
            [(0, 0), (0, 1), (0, 2), (0, 3)],
        )

    def test_line_default_placed_correctly(self):
        self.assertEqual(
            tetris_block.Block(shape=1).block, [(5, 0), (5, 1), (5, 2), (5, 3)]
        )

    def test_line_move_down(self):
        self.line.move_down()
        self.assertEqual(self.line.block, [(5, 1), (5, 2), (5, 3), (5, 4)])

    def test_line_move_left(self):
        self.line.move_left()
        self.assertEqual(self.line.block, [(4, 0), (4, 1), (4, 2), (4, 3)])

    def test_line_move_right(self):
        self.line.move_right()
        self.assertEqual(self.line.block, [(6, 0), (6, 1), (6, 2), (6, 3)])

    def test_line_down_no_oob(self):
        line = tetris_block.Block(x_coord=5, y_coord=16, shape=1)
        self.assertEqual(line.block, [(5, 16), (5, 17), (5, 18), (5, 19)])
        line.move_down()
        self.assertEqual(line.block, [(5, 16), (5, 17), (5, 18), (5, 19)])

    def test_line_left_no_oob(self):
        line = tetris_block.Block(x_coord=0, y_coord=0, shape=1)
        self.assertEqual(line.block, [(0, 0), (0, 1), (0, 2), (0, 3)])
        line.move_left()
        self.assertEqual(line.block, [(0, 0), (0, 1), (0, 2), (0, 3)])

    def test_line_right_no_oob(self):
        line = tetris_block.Block(x_coord=9, y_coord=0, shape=1)
        self.assertEqual(line.block, [(9, 0), (9, 1), (9, 2), (9, 3)])
        line.move_right()
        self.assertEqual(line.block, [(9, 0), (9, 1), (9, 2), (9, 3)])

    def test_iterator_returns_points(self):
        output = []
        for point in self.line:
            output.append(point)
        self.assertEqual(output, [(5, 0), (5, 1), (5, 2), (5, 3)])
