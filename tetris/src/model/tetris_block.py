
SHAPES = {0: ((0,0),(0,1),(1,0),(1,1))}

class Block:
    def __init__(self, x=5, y=0, shape=0):
        self.block = []
        self.shape = shape
        for point in SHAPES[shape]:
            self.block.append((point[0]+x, point[1]+y))
    
    def move_down(self):
        new_pos = []
        for point in self.block:
            new_point = (point[0], point[1]+1)
            if new_point[1] > 19:
                return
            new_pos.append(new_point)
        self.block = new_pos
    
    def move_left(self):
        new_pos = []
        for point in self.block:
            new_point = (point[0]-1, point[1])
            if new_point[0] < 0:
                return
            new_pos.append(new_point)
        self.block = new_pos
    
    def move_right(self):
        new_pos = []
        for point in self.block:
            new_point = (point[0]+1, point[1])
            if new_point[0] > 9:
                return
            new_pos.append(new_point)
        self.block = new_pos
    
    def __iter__(self):
        return (point for point in self.block)
        
