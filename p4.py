import random

class Node:
    
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.visited = False

    def setVisited(self):
        self.visited = True

    def getVisited(self):
        return self.visited

class DirectedGraph:
    def __init__(self):
        self.nodes = []

    def addNode(self, val):
        node = Node(val)
        self.nodes.append(node)

    def addDirectedEdge(self, first, second):
        if second not in first.neighbors:
            first.neighbors.add(second)
    
    def removeDirectedEdge(self, first, second):
        if second in first.neighbors:
            first.neighbors.remove(second)

    def getAllNodes(self):
        return set(self.nodes)


class TopSort:

    @classmethod
    def Kahns(cls, graph):
        inDeg = {}
        l = []
        for node in graph.getAllNodes():
            inDeg[node] = 0
            l += list(node.neighbors)
            
        for node in l:
            inDeg[node] += 1

        ret = []
        queue = []

        for node in inDeg:
            if inDeg[node] == 0:
                queue.append(node)
                inDeg[node] -= 1

        while len(queue) > 0:
            n = queue.pop(0)
            ret.append(n)
            for node in n.neighbors:
                inDeg[node] -= 1
                if inDeg[node] == 0:
                    queue.append(node)
            inDeg[n] -= 1

        return ret

    @classmethod
    def mDFS(cls, graph):
        stack = []
        visited = []

        for node in graph.getAllNodes():
            if not node.getVisited():
                cls.mDFSHelper(node, stack)
        
        return [val for val in reversed(stack)]

    @classmethod
    def mDFSHelper(cls, node, stack):
        node.setVisited()
        for neighbor in node.neighbors:
            if not neighbor.getVisited():
                cls.mDFSHelper(neighbor, stack)
        stack.append(node)

def createRandomDAGIter(n):
    # might have to fix acyclic portion
    g = DirectedGraph()
    for i in range(n):
        g.addNode(random.randint(0, 10*n))
    for i in range(random.randint(1, n - 1)):
        g.addDirectedEdge(random.sample(g.getAllNodes(), 1)[0], random.sample(g.getAllNodes(), 1)[0])

    return g

graph = DirectedGraph()

graph.addNode('A')
graph.addNode('B')
graph.addNode('C')
graph.addNode('D')
graph.addNode('E')
graph.addNode('F')
graph.addNode('G')
graph.addNode('H')

graph.nodes[0].neighbors = set([graph.nodes[1], graph.nodes[3]])
graph.nodes[2].neighbors = set([graph.nodes[3], graph.nodes[6], graph.nodes[7]])
graph.nodes[3].neighbors = set([graph.nodes[6]])
graph.nodes[7].neighbors = set([graph.nodes[4], graph.nodes[5]])

def printvals(lst):
    for i in range(len(lst)-1):
        print(lst[i].val, end=" -> ")
    if len(lst) > 0:
        print(lst[-1].val)

rand = createRandomDAGIter(1000)

printvals(TopSort.Kahns(rand))
printvals(TopSort.mDFS(rand))
