import Node

# handles a weighted Node
class NodeW(Node.Node):
    
    def __init__(self, val: int):
        self.val = val
        self.neighbors = set()
        self.weights = {}