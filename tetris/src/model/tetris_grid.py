
class Grid:
    def __init__(self):
        self._grid = [[False for i in range(0,10)] for i in range(0,20)]

    def update(self, x, y, state: bool):
        self._grid[y][x] = state
    
    def get(self, x, y) -> bool:
        return self._grid[y][x]
    
    def __iter__(self):
        for y in range(0, len(self._grid)):
            for x in range(0, len(self._grid[0])):
                yield self._grid[y][x], x, y