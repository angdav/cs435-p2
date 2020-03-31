import random

class Node:
    
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.weights = {}

class WeightedGraph:
    def __init__(self):
        self.nodes = []

    def addNode(self, val):
        node = Node(val)
        self.nodes.append(node)

    def addWeightedEdge(self, first, second, edgeWeight):
        if second not in first.neighbors:
            first.neighbors.add(second)
            first.weights[second] = edgeWeight
    
    def removeWeightedEdge(self, first, second):
        if second in first.neighbors:
            first.neighbors.remove(second)
            del first.weights[second]

    def getAllNodes(self):
        return set(self.nodes)

def createRandomCompleteWeightedGraph(n):
    g = WeightedGraph()
    for i in range(n):
        g.addNode(i)
    for node in g.getAllNodes():
        for node2 in g.getAllNodes():
            if node != node2:
                g.addWeightedEdge(node, node2, random.randint(1,10))
    return g

graph = createRandomCompleteWeightedGraph(100)

