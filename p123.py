import random

class Node:
    
    def __init__(self, val):
        self.val = val
        self.neighbors = set()

class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, val):
        node = Node(val)
        self.nodes.append(node)

    def addUndirectedEdge(self, first, second):
        if second not in first.neighbors:
            first.neighbors.add(second)
        if first not in second.neighbors:
            second.neighbors.add(first)
    
    def removeUndirectedEdge(self, first, second):
        if second in first.neighbors:
            first.neighbors.remove(second)
        if first in second.neighbors:
            second.neighbors.remove(first)

    def getAllNodes(self):
        return set(self.nodes)

class GraphSearch:
    
    @classmethod
    def DFSRec(cls, start, end):
        return cls.DFSRecHelper(start, end, set([start]), [start], [])

    @classmethod
    def DFSRecHelper(cls, start, end, visited, stack, traversal):
        if len(stack) > 0:
            curr = stack.pop()
            traversal.append(curr)
            if curr == end:
                return traversal
            for v in curr.neighbors:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
            return cls.DFSRecHelper(start, end, visited, stack, traversal)
    
    @classmethod
    def DFSIter(cls, start, end):
        visited = set()
        stack = [start]
        visited.add(start)
        traversal = []

        while len(stack) > 0:
            curr = stack.pop()
            traversal.append(curr)
            if curr == end:
                return traversal
            for v in curr.neighbors:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        return None

    @classmethod
    def BFTIter(cls, graph):
        visited = set()
        queue = []
        traversal = []
        for node in graph.nodes:
            if node not in visited:
                visited.add(node)
                queue.insert(0, node)
            while len(queue) > 0:
                curr = queue.pop()
                traversal.append(curr)
                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.insert(0, neighbor)
        return traversal

    @classmethod
    def BFTRec(cls, graph):
        return cls.BFTRecHelper(graph, set(), [], [])

    @classmethod
    def BFTRecHelper(cls, graph, visited, queue, traversal):
        if len(queue) == 0:
            for node in graph.nodes:
                if node not in visited:
                    visited.add(node)
                    queue.insert(0, node)
                    return cls.BFTRecHelper(graph, visited, queue, traversal)
            return traversal
        curr = queue.pop()
        traversal.append(curr)
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.insert(0, neighbor)
        return cls.BFTRecHelper(graph, visited, queue, traversal)

def createRandomUnweightedGraphIter(n):
    g = Graph()
    for i in range(n):
        g.addNode(random.randint(0, 10*n))
    for i in range(random.randint(1, n - 1)):
        g.addUndirectedEdge(random.sample(g.getAllNodes(), 1)[0], random.sample(g.getAllNodes(), 1)[0])

    return g

def createLinkedList(n):
    g = Graph()
    g.addNode(0)
    for i in range(1, n):
        g.addNode(i)
        g.nodes[i-1].neighbors.add(g.nodes[i])
    return g

def BFTRecLinkedList():
    ll = createLinkedList(10000)
    GraphSearch.BFTRec(ll)

def BFTIterLinkedList():
    ll = createLinkedList(10000)
    GraphSearch.BFTIter(ll)

graph = Graph()

for i in range(14):
    graph.addNode(i)

graph.nodes[0].neighbors = set([graph.nodes[7], graph.nodes[3], graph.nodes[4], graph.nodes[1]])
graph.nodes[1].neighbors = set([graph.nodes[0], graph.nodes[2], graph.nodes[11]])
graph.nodes[2].neighbors = set([graph.nodes[1], graph.nodes[13]])
graph.nodes[3].neighbors = set([graph.nodes[0], graph.nodes[4]])
graph.nodes[4].neighbors = set([graph.nodes[3], graph.nodes[0], graph.nodes[5], graph.nodes[6]])
graph.nodes[5].neighbors = set([graph.nodes[6], graph.nodes[4]])
graph.nodes[6].neighbors = set([graph.nodes[4], graph.nodes[5]])
graph.nodes[7].neighbors = set([graph.nodes[8], graph.nodes[0], graph.nodes[12], graph.nodes[11]])
graph.nodes[8].neighbors = set([graph.nodes[9], graph.nodes[7]])
graph.nodes[9].neighbors = set([graph.nodes[8]])
graph.nodes[10].neighbors = set([])
graph.nodes[11].neighbors = set([graph.nodes[12], graph.nodes[7], graph.nodes[1]])
graph.nodes[12].neighbors = set([graph.nodes[7], graph.nodes[11]])
graph.nodes[13].neighbors = set([graph.nodes[2]])

def printvals(lst):
    for i in range(len(lst)-1):
        print(lst[i].val, end=" -> ")
    if len(lst) > 0:
        print(lst[-1].val)

printvals(GraphSearch.DFSIter(graph.nodes[0], graph.nodes[9]))
printvals(GraphSearch.DFSRec(graph.nodes[0], graph.nodes[9]))
printvals(GraphSearch.BFTIter(graph))
printvals(GraphSearch.BFTRec(graph))

BFTIterLinkedList()
BFTRecLinkedList()