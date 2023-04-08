
class Grid:
    def __init__(self):
        self.rows = 20
        self.columns = 10
        self._grid = [[False for i in range(0,self.columns)] for i in range(0,self.rows)]

    def update(self, x, y, state: bool):
        self._grid[y][x] = state
    
    def get(self, x, y) -> bool:
        return self._grid[y][x]
    
    def check_row(self, y):
        for x in self._grid[y]:
            if not x:
                return False
        return True
    
    def shift_down_over(self, y):
        if y == 0:
            self._grid[0] = [False for i in range(0,self.columns)]
            return
        fresh_row = [False for i in range(0,self.columns)]
        del self._grid[y]
        self._grid = [fresh_row] + self._grid

    
    def __iter__(self):
        for y in range(0, len(self._grid)):
            for x in range(0, len(self._grid[0])):
                yield self._grid[y][x], x, y