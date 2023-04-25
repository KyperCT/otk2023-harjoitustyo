# 0 : Square, 1: line, 2: T-block, 3: L-block, 4: Backwards L, 5: S-block, 6: Backwards S
SHAPES = {
    0: ((0, 0), (0, 1), (1, 0), (1, 1)),
    1: ((0, 0), (0, 1), (0, 2), (0, 3)),
    2: ((0, 0), (0, 1), (1, 1), (0, 2)),
    3: ((0, 0), (0, 1), (0, 2), (1, 2)),
    4: ((0, 0), (0, 1), (0, 2), (-1, 2)),
    5: ((0, 0), (0, 1), (1, 1), (1, 2)),
    6: ((0, 0), (0, 1), (-1, 1), (-1, 2)),
}


class Block:
    def __init__(self, x_coord=5, y_coord=0, shape=0):
        self.block = []
        self.shape = shape
        for point in SHAPES[shape]:
            self.block.append((point[0] + x_coord, point[1] + y_coord))
        self._past_block = self.block
    
    def unmove(self):
        self.block = self._past_block

    def move_down(self):
        new_pos = []
        for point in self.block:
            new_point = (point[0], point[1] + 1)
            if new_point[1] > 19:
                return
            new_pos.append(new_point)
        self._past_block = self.block
        self.block = new_pos

    def move_left(self):
        new_pos = []
        for point in self.block:
            new_point = (point[0] - 1, point[1])
            if new_point[0] < 0:
                return
            new_pos.append(new_point)
        self._past_block = self.block
        self.block = new_pos

    def move_right(self):
        new_pos = []
        for point in self.block:
            new_point = (point[0] + 1, point[1])
            if new_point[0] > 9:
                return
            new_pos.append(new_point)
        self._past_block = self.block
        self.block = new_pos

    def __iter__(self):
        return (point for point in self.block)
