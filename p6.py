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
    # Note: Likelihood changed to 80% so that a path to destNode exists almost every time
    for node in g.getAllNodes():
        if node.x - 1 >= 0 and frozenset([node, g.nodes[(node.x-1, node.y)]]) not in tried:
            tried.add(frozenset([node, g.nodes[(node.x-1, node.y)]]))
            if random.randint(1, 10) <= 8:
                g.addUndirectedEdge(node, g.nodes[(node.x-1, node.y)])
        if node.x + 1 < n and frozenset([node, g.nodes[(node.x+1, node.y)]]) not in tried:
            tried.add(frozenset([node, g.nodes[(node.x+1, node.y)]]))
            if random.randint(1, 10) <= 8:
                g.addUndirectedEdge(node, g.nodes[(node.x+1, node.y)])
        if node.y - 1 >= 0 and frozenset([node, g.nodes[(node.x, node.y-1)]]) not in tried:
            tried.add(frozenset([node, g.nodes[(node.x, node.y-1)]]))
            if random.randint(1, 10) <= 8:
                g.addUndirectedEdge(node, g.nodes[(node.x, node.y-1)])
        if node.y + 1 < n and frozenset([node, g.nodes[(node.x, node.y+1)]]) not in tried:
            tried.add(frozenset([node, g.nodes[(node.x, node.y+1)]]))
            if random.randint(1, 10) <= 8:
                g.addUndirectedEdge(node, g.nodes[(node.x, node.y+1)])
    
    return g

def manhattanDistance(node, destNode):
    return abs(node.x - destNode.x) + abs(node.y - destNode.y)
    
def minDistance(d, visited):
    ans = None
    m = float('inf')
    for node in d:
        if node not in visited and d[node][0] + d[node][1] <= m:
            m = d[node][0] + d[node][1]
            ans = node
    return ans

def astar(sourceNode, destNode):
    d = {}
    # g, h, parentNode
    d[sourceNode] = (0, manhattanDistance(sourceNode, destNode), None)
    curr = sourceNode
    visited = set()

    while curr and curr != destNode:
        visited.add(curr)
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                newD = d[curr][0]
                h = manhattanDistance(neighbor, destNode)
                if neighbor not in d or newD + h < d[neighbor][0] + d[neighbor][1]:
                    d[neighbor] = (newD, h, curr)
        curr = minDistance(d, visited)

    path = destNode
    traversal = []
    while path:
        traversal.insert(0, path)
        if path in d:
            path = d[path][2]
        else:
            return [] # means no path to goal

    return traversal

def printvals(lst):
    for i in range(len(lst)-1):
        print(lst[i].val, end=" -> ")
    if len(lst) > 0:
        print(lst[-1].val)

if __name__ == "__main__":   
    g = createRandomGridGraph(10)
    sourceNode = g.nodes[(0, 0)]
    destNode = g.nodes[(9, 9)]
    printvals(astar(sourceNode, destNode))

    graph = GridGraph()

    graph.addGridNode(0, 0, 'A') # 0
    graph.addGridNode(1, 0, 'B') # 1
    graph.addGridNode(2, 0, 'C') # 2
    graph.addGridNode(0, 1, 'D') # 3
    graph.addGridNode(1, 1, 'E') # 4
    graph.addGridNode(2, 1, 'F') # 5
    graph.addGridNode(0, 2, 'G') # 6

    #   G
    #   |
    #   D - E - F
    #   |   |   |
    #   A - B - C

    graph.addUndirectedEdge(graph.nodes[(0,0)], graph.nodes[(1,0)])
    graph.addUndirectedEdge(graph.nodes[(0,0)], graph.nodes[(0,1)])
    graph.addUndirectedEdge(graph.nodes[(1,0)], graph.nodes[(2,0)])
    graph.addUndirectedEdge(graph.nodes[(1,0)], graph.nodes[(1,1)])
    graph.addUndirectedEdge(graph.nodes[(2,0)], graph.nodes[(2,1)])
    graph.addUndirectedEdge(graph.nodes[(1,1)], graph.nodes[(2,1)])
    graph.addUndirectedEdge(graph.nodes[(1,1)], graph.nodes[(0,1)])
    graph.addUndirectedEdge(graph.nodes[(0,1)], graph.nodes[(0,2)])

    src = graph.nodes[(0,0)]
    dest = graph.nodes[(0,2)]

    printvals(astar(src, dest))