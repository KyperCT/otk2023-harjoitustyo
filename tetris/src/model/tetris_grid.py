class Grid:
    """Tetris grid object. Stores which points have blocks and which do not.

    Attributes:
      rows: rows in grid
      columns: columns in grid
      _grid: internal data structure for grid
    """
    def __init__(self):
        """Constructor for object, makes new empty grid
        """
        self.rows = 20
        self.columns = 10
        self._grid = [
            [False for i in range(0, self.columns)] for i in range(0, self.rows)
        ]

    def update(self, column, row, state: bool):
        """Changes if a point in the grid is occupied.

        Args:
          column: which column the point is in
          row: which row the point is in
          state: if True makes the point occupied, if False unoccupied
        """
        self._grid[row][column] = state

    def get(self, column, row) -> bool:
        """Gets if a point is occupied

        Args:
          column: which column the point is in
          row: which row the point is in
        
        Returns:
          True if occupied, False if not
        """
        return self._grid[row][column]

    def check_row(self, row):
        """Gets if a row is fully occupied

        Args:
          row: which row to check
        
        Returns:
          True if all points are occupied, False if not
        """
        for column in self._grid[row]:
            if not column:
                return False
        return True

    def shift_down_over(self, row):
        """Removes a row and shifts rows above it down by one
        (shifts rows down over top of the old row)

        Args:
          row: which row to remove
        """
        if row == 0:
            self._grid[0] = [False for i in range(0, self.columns)]
            return
        fresh_row = [False for i in range(0, self.columns)]
        del self._grid[row]
        self._grid = [fresh_row] + self._grid

    def clear(self):
        """Makes the entire grid unoccupied
        """
        self._grid = [
            [False for i in range(0, self.columns)] for i in range(0, self.rows)
        ]

    def __iter__(self):
        """Allows the grid to be iterated over, left to right, top to bottom
        
        Yields:
          Next point
        """
        for row in range(0, len(self._grid)):
            for column in range(0, len(self._grid[0])):
                yield self._grid[row][column], column, row
