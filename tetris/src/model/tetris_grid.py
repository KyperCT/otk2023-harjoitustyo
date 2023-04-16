class Grid:
    def __init__(self):
        self.rows = 20
        self.columns = 10
        self._grid = [
            [False for i in range(0, self.columns)] for i in range(0, self.rows)
        ]

    def update(self, column, row, state: bool):
        self._grid[row][column] = state

    def get(self, column, row) -> bool:
        return self._grid[row][column]

    def check_row(self, row):
        for column in self._grid[row]:
            if not column:
                return False
        return True

    def shift_down_over(self, row):
        if row == 0:
            self._grid[0] = [False for i in range(0, self.columns)]
            return
        fresh_row = [False for i in range(0, self.columns)]
        del self._grid[row]
        self._grid = [fresh_row] + self._grid

    def __iter__(self):
        for row in range(0, len(self._grid)):
            for column in range(0, len(self._grid[0])):
                yield self._grid[row][column], column, row
