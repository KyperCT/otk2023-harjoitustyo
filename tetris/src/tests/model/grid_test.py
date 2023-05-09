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
        for i in range(0, 10):
            self.grid.update(i, 1, True)
        self.assertEqual(self.grid.check_row(1), True)

    def test_clear_clears_grid(self):
        self.grid.update(4, 5, True)
        self.grid.update(7, 12, True)
        self.grid.update(1, 15, True)
        self.grid.update(2, 7, True)
        self.grid.update(3, 15, True)
        self.grid.update(8, 19, True)

        self.grid.clear()

        is_not_empty = False
        for point in self.grid:
            if point[0]:
                is_not_empty = True
        self.assertEqual(is_not_empty, False)

    def test_shift_down_over_works(self):
        self.grid.update(4, 5, True)
        self.grid.update(7, 12, True)
        self.grid.update(1, 15, True)
        self.grid.update(2, 7, True)
        self.grid.update(3, 15, True)
        self.grid.update(8, 19, True)

        self.grid.shift_down_over(15)
        new_filled_points = [(4, 6), (7, 13), (2, 8), (8, 19)]
        any_wrong_values = False
        for point in self.grid:
            if (point[1], point[2]) in new_filled_points:
                if not point[0]:
                    any_wrong_values = True
            else:
                if point[0]:
                    any_wrong_values = True
        self.assertEqual(any_wrong_values, False)

    def test_shift_down_over_works_at_row_0(self):
        self.grid.update(4, 5, True)
        self.grid.update(7, 12, True)
        self.grid.update(1, 0, True)
        self.grid.update(2, 7, True)
        self.grid.update(3, 0, True)
        self.grid.update(8, 19, True)

        self.grid.shift_down_over(0)
        new_filled_points = [(4, 5), (7, 12), (2, 7), (8, 19)]
        any_wrong_values = False
        for point in self.grid:
            if (point[1], point[2]) in new_filled_points:
                if not point[0]:
                    any_wrong_values = True
            else:
                if point[0]:
                    any_wrong_values = True
        self.assertEqual(any_wrong_values, False)
