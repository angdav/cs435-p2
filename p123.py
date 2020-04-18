import random
import Graph
import GraphSearch

def createRandomUnweightedGraphIter(n: int) -> Graph:
    g = Graph.Graph()
    taken = set()
    for i in range(n):
        gen = random.randint(0, 10*n)
        while gen in taken:
            gen = random.randint(0, 10*n)
        g.addNode(gen)
        taken.add(gen)
    for i in range(random.randint(1, n - 1)):
        g.addUndirectedEdge(random.sample(g.getAllNodes(), 1)[0], random.sample(g.getAllNodes(), 1)[0])

    return g

def createLinkedList(n: int) -> Graph:
    g = Graph.Graph()
    if n == 0:
        return g
    g.addNode(0)
    for i in range(1, n):
        g.addNode(i)
        g.nodes[i-1].neighbors.add(g.nodes[i])
    return g

def BFTRecLinkedList() -> None:
    ll = createLinkedList(10000)
    GraphSearch.GraphSearch.BFTRec(ll)

def BFTIterLinkedList() -> None:
    ll = createLinkedList(10000)
    GraphSearch.GraphSearch.BFTIter(ll)

if __name__ == "__main__":
    graph = Graph.Graph()

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

    # REQUIRED ASSIGNMENT TEST CASES BELOW
    printvals(GraphSearch.GraphSearch.DFSIter(graph.nodes[0], graph.nodes[9]))
    printvals(GraphSearch.GraphSearch.DFSRec(graph.nodes[0], graph.nodes[9]))
    printvals(GraphSearch.GraphSearch.BFTIter(graph))
    printvals(GraphSearch.GraphSearch.BFTRec(graph))

    BFTIterLinkedList()
    BFTRecLinkedList()