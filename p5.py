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

def createLinkedList(n):
    g = WeightedGraph()
    g.addNode(0)
    for i in range(1, n):
        g.addNode(i)
        g.addWeightedEdge(g.nodes[i-1], g.nodes[i], 1)
    return g

ll = createLinkedList(100)

def minDistance(d, visited):
    ans = None
    m = float('inf')
    for node in d:
        if node not in visited and d[node] <= m:
            m = d[node]
            ans = node
    return ans

def dijkstras(start):
    d = {}
    d[start] = 0
    visited = set()

    while start and start in d:
        visited.add(start)
        for neighbor in start.neighbors:
            if neighbor not in visited:
                newD = d[start] + start.weights[neighbor]
                if neighbor not in d or newD < d[neighbor]:
                    d[neighbor] = newD
        start = minDistance(d, visited)

    return d

if __name__ == "__main__":
    graph = WeightedGraph()

    graph.addNode('A') # 0
    graph.addNode('B') # 1
    graph.addNode('C') # 2
    graph.addNode('D') # 3
    graph.addNode('E') # 4
    graph.addNode('F') # 5
    graph.addNode('G') # 6

    graph.addWeightedEdge(graph.nodes[0], graph.nodes[1], 2)
    graph.addWeightedEdge(graph.nodes[1], graph.nodes[0], 2)

    graph.addWeightedEdge(graph.nodes[0], graph.nodes[2], 4)
    graph.addWeightedEdge(graph.nodes[2], graph.nodes[0], 4)

    graph.addWeightedEdge(graph.nodes[0], graph.nodes[3], 7)
    graph.addWeightedEdge(graph.nodes[3], graph.nodes[0], 7)

    graph.addWeightedEdge(graph.nodes[0], graph.nodes[5], 5)
    graph.addWeightedEdge(graph.nodes[5], graph.nodes[0], 5)

    graph.addWeightedEdge(graph.nodes[2], graph.nodes[5], 6)
    graph.addWeightedEdge(graph.nodes[5], graph.nodes[2], 6)

    graph.addWeightedEdge(graph.nodes[3], graph.nodes[5], 10)
    graph.addWeightedEdge(graph.nodes[5], graph.nodes[3], 10)

    graph.addWeightedEdge(graph.nodes[3], graph.nodes[6], 6)
    graph.addWeightedEdge(graph.nodes[6], graph.nodes[3], 6)

    graph.addWeightedEdge(graph.nodes[5], graph.nodes[6], 6)
    graph.addWeightedEdge(graph.nodes[6], graph.nodes[5], 6)

    graph.addWeightedEdge(graph.nodes[1], graph.nodes[3], 6)
    graph.addWeightedEdge(graph.nodes[3], graph.nodes[1], 6)

    graph.addWeightedEdge(graph.nodes[1], graph.nodes[4], 3)
    graph.addWeightedEdge(graph.nodes[4], graph.nodes[1], 3)

    graph.addWeightedEdge(graph.nodes[1], graph.nodes[6], 8)
    graph.addWeightedEdge(graph.nodes[6], graph.nodes[1], 8)

    graph.addWeightedEdge(graph.nodes[4], graph.nodes[6], 7)
    graph.addWeightedEdge(graph.nodes[6], graph.nodes[4], 7)

    dijkstras = dijkstras(graph.nodes[0])
    for key in dijkstras:
        print('{}: {}'.format(key.val, dijkstras[key]))