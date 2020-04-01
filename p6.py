import random

class GridNode:
    
    def __init__(self, x, y, val):
        self.val = val
        self.x = x
        self.y = y
        self.neighbors = set()

class WeightedGraph:
    def __init__(self):
        self.nodes = []

    def addGridNode(self, x, y, nodeVal):
        node = GridNode(x, y, nodeVal)
        self.nodes.append(node)

    def addUndirectedEdge(self, first, second):
        if (abs(first.x - second.x) == 1) != (abs(first.y - second.y) == 1):
            if second not in first.neighbors:
                first.neighbors.add(second)
            if first not in second.neighbors:
                second.neighbors.add(first)
    
    def removeUndirectedEdge(self, first, second):
        if second in first.neighbors:
            first.neighbors.remove(second)
        if first not in second.neighbors:
            second.neighbors.add(first)

    def getAllNodes(self):
        return set(self.nodes)

def createRandomGridGraph(n):
    g = WeightedGraph()
    for i in range(n):
        for j in range(n):
            g.addGridNode(i, j, n*i + j)

    tried = set()
    for node in g.getAllNodes():
        for node2 in g.getAllNodes():
            if (abs(node.x - node2.x) == 1 and abs(node.y - node2.y) == 0) or (abs(node.x - node2.x) == 0 and abs(node.y - node2.y) == 1):
                if frozenset([node, node2]) not in tried:
                    tried.add(frozenset([node, node2]))
                    g.addUndirectedEdge(node, node2)
    
    return g

g = createRandomGridGraph(10)