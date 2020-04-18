import GridNode
import Graph

class GridGraph(Graph.Graph):

    def __init__(self):
        self.nodes = {}

    def addGridNode(self, x: int, y: int, nodeVal: int) -> None:
        node = GridNode.GridNode(x, y, nodeVal)
        self.nodes[(x,y)] = node

    def addUndirectedEdge(self, first: GridNode, second: GridNode) -> None:
        if (abs(first.x - second.x) == 1) != (abs(first.y - second.y) == 1):
            if second not in first.neighbors:
                first.neighbors.add(second)
            if first not in second.neighbors:
                second.neighbors.add(first)
    
    def removeUndirectedEdge(self, first: GridNode, second: GridNode) -> None:
        if second in first.neighbors:
            first.neighbors.remove(second)
        if first not in second.neighbors:
            second.neighbors.remove(first)

    def getAllNodes(self) -> set:
        return set(self.nodes.values())