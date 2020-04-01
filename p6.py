import random

class GridNode:
    
    def __init__(self, x, y, val):
        self.val = val
        self.x = x
        self.y = y
        self.neighbors = set()

class GridGraph:
    def __init__(self):
        self.nodes = {}

    def addGridNode(self, x, y, nodeVal):
        node = GridNode(x, y, nodeVal)
        self.nodes[(x,y)] = node

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
        return set(self.nodes.values())

def createRandomGridGraph(n):
    g = GridGraph()
    for i in range(n):
        for j in range(n):
            g.addGridNode(i, j, n*i + j)

    tried = set()
    for node in g.getAllNodes():
        if node.x - 1 >= 0 and frozenset([node, g.nodes[(node.x-1, node.y)]]) not in tried:
            tried.add(frozenset([node, g.nodes[(node.x-1, node.y)]]))
            if random.randint(0, 1) == 1:
                g.addUndirectedEdge(node, g.nodes[(node.x-1, node.y)])
        if node.x + 1 < n and frozenset([node, g.nodes[(node.x+1, node.y)]]) not in tried:
            tried.add(frozenset([node, g.nodes[(node.x+1, node.y)]]))
            if random.randint(0, 1) == 1:
                g.addUndirectedEdge(node, g.nodes[(node.x+1, node.y)])
        if node.y - 1 >= 0 and frozenset([node, g.nodes[(node.x, node.y-1)]]) not in tried:
            tried.add(frozenset([node, g.nodes[(node.x, node.y-1)]]))
            if random.randint(0, 1) == 1:
                g.addUndirectedEdge(node, g.nodes[(node.x, node.y-1)])
        if node.y + 1 < n and frozenset([node, g.nodes[(node.x, node.y+1)]]) not in tried:
            tried.add(frozenset([node, g.nodes[(node.x, node.y+1)]]))
            if random.randint(0, 1) == 1:
                g.addUndirectedEdge(node, g.nodes[(node.x, node.y+1)])
    
    return g

g = createRandomGridGraph(100)
sourceNode = g.nodes[(0, 0)]
print(sourceNode.x, sourceNode.y)