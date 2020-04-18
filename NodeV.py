import Node

# handles a Node with a visited attribute
class NodeV(Node.Node):
    
    def __init__(self, val: int):
        self.val = val
        self.neighbors = set()
        self.__visited = False

    def setVisited(self) -> None:
        self.__visited = True

    def getVisited(self) -> None:
        return self.__visited