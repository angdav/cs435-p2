import Node

# handles a Node with x and y coordinates
class GridNode(Node.Node):
    
    def __init__(self, x: int, y: int, val: int):
        self.val = val
        self.x = x
        self.y = y
        self.neighbors = set()