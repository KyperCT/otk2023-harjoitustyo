# 0 : Square, 1: line, 2: T-block, 3: L-block, 4: Backwards L, 5: S-block, 6: Backwards S
SHAPES = {
    0: ((0.5, 0.5), ((-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5))),
    1: ((-0.5, 1.5), ((0.5, -1.5), (0.5, -0.5), (0.5, 0.5), (0.5, 1.5))),
    2: ((0, 1), ((0, -1), (0, 0), (1, 0), (0, 1))),
    3: ((0, 1), ((0, -1), (0, 0), (0, 1), (1, 1))),
    4: ((0, 1), ((0, -1), (0, 0), (0, 1), (-1, 1))),
    5: ((0, 1), ((0, -1), (0, 0), (1, 0), (1, 1))),
    6: ((0, 1), ((0, -1), (0, 0), (-1, 0), (-1, 1))),
}
ROTATION_GRIDS = {
    "odd": [
        [(-1, -1), (0, -1), (1, -1)],
        [(-1, 0), (0, 0), (1, 0)],
        [(-1, 1), (0, 1), (1, 1)],
    ],
    "even": [
        [(-1.5, -1.5), (-0.5, -1.5), (0.5, -1.5), (1.5, -1.5)],
        [(-1.5, -0.5), (-0.5, -0.5), (0.5, -0.5), (1.5, -0.5)],
        [(-1.5, 0.5), (-0.5, 0.5), (0.5, 0.5), (1.5, 0.5)],
        [(-1.5, 1.5), (-0.5, 1.5), (0.5, 1.5), (1.5, 1.5)],
    ],
}


class Block:
    """Tetris block object, defines shape and points of block

    Attributes:
      block: points the block occupies as tuples
      shape: Int, which shape type the block is
      rotation_grid: matrix grid used to calculate rotation
      center: the point of the block center
      _transposed: whether the rotation grid has been transposed
      _past_block: stores block before move for unmove
      _rotate_last: stores whether the block was rotated for unmove
    """
    def __init__(self, x_coord=5, y_coord=0, shape=0):
        """Constructor for block object

        Args:
          x_coord: x co-ordinate to construct block at
          y_coord: y co-ordinate to construct block at
          shape: which shapetype to build
        """
        self.block = []
        self.shape = shape
        if shape < 2:
            self.rotation_grid = ROTATION_GRIDS["even"]
        else:
            self.rotation_grid = ROTATION_GRIDS["odd"]
        self._transposed = False
        self.center = [SHAPES[shape][0][0] + x_coord, SHAPES[shape][0][1] + y_coord]
        for point in SHAPES[shape][1]:
            self.block.append(
                (int(point[0] + self.center[0]), int(point[1] + self.center[1]))
            )
        self._past_block = self.block
        self._rotate_last = False

    def unmove(self):
        """Returns block into previous state after a move.

        Can only undo once
        """
        self.block = self._past_block
        if self._rotate_last:
            if self._transposed:
                self._transposed = False
            else:
                self._transposed = True

    def move_down(self):
        """Moves block down by one

        will not move under y 19
        """
        new_pos = []
        for point in self.block:
            new_point = (point[0], point[1] + 1)
            if new_point[1] > 19:
                return
            new_pos.append(new_point)
        self._past_block = self.block
        self.block = new_pos
        self.center[1] += 1
        self._rotate_last = False

    def move_left(self):
        """Moves block left by one

        will not move past x 0
        """
        new_pos = []
        for point in self.block:
            new_point = (point[0] - 1, point[1])
            if new_point[0] < 0:
                return
            new_pos.append(new_point)
        self._past_block = self.block
        self.block = new_pos
        self.center[0] += -1
        self._rotate_last = False

    def move_right(self):
        """Moves block right by one

        will not move past x 9
        """
        new_pos = []
        for point in self.block:
            new_point = (point[0] + 1, point[1])
            if new_point[0] > 9:
                return
            new_pos.append(new_point)
        self._past_block = self.block
        self.block = new_pos
        self.center[0] += 1
        self._rotate_last = False

    def _rotate_grid(self):
        """Rotates rotation grid used for block rotation (matrix rotation)
        """
        if self._transposed:
            self._transposed = False
        else:
            self._transposed = True

        if self._transposed:
            for i in range(0, len(self.rotation_grid)):
                swapspace = self.rotation_grid[0][i]
                self.rotation_grid[0][i] = self.rotation_grid[-1][i]
                self.rotation_grid[-1][i] = swapspace
                if len(self.rotation_grid) > 3:
                    swapspace = self.rotation_grid[1][i]
                    self.rotation_grid[1][i] = self.rotation_grid[-2][i]
                    self.rotation_grid[-2][i] = swapspace
        else:
            for row in self.rotation_grid:
                row.reverse()

    def move_rotate(self):
        """Rotates block by 90 degrees clockwise

        will not rotate past bounds x 0 or x 9
        """
        new_pos = []
        self._rotate_grid()
        if len(self.rotation_grid) == 3:
            index_center = (1, 1)
        else:
            index_center = (1.5, 1.5)
        for point in SHAPES[self.shape][1]:
            index_point = (
                int(point[1] + index_center[0]),
                int(point[0] + index_center[1]),
            )
            if self._transposed:
                index_point = (index_point[1], index_point[0])
            grid_point = self.rotation_grid[index_point[0]][index_point[1]]
            new_point = (
                int(self.center[0] + grid_point[0]),
                int(self.center[1] + grid_point[1]),
            )
            if (new_point[0]<0) or (new_point[0]>9):
                return
            new_pos.append(new_point)

        self._past_block = self.block
        self.block = new_pos
        self._rotate_last = True

    def __iter__(self):
        """Provides iterator for tetris block

        Returns:
          generator, which iterates over points in block
        """
        return (point for point in self.block)
