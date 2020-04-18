import random
import NodeV
import DirectedGraph
import TopSort

def createRandomDAGIter(n: int) -> DirectedGraph:
    g = DirectedGraph.DirectedGraph()
    taken = set()
    for i in range(n):
        g.addNode(random.randint(0, 10*n))
    for i in range(random.randint(1, n - 1)):
        first = random.sample(g.getAllNodes(), 1)[0]
        second = random.sample(g.getAllNodes(), 1)[0]
        if first != second and (first not in taken or second not in taken):
            g.addDirectedEdge(random.sample(g.getAllNodes(), 1)[0], random.sample(g.getAllNodes(), 1)[0])
            taken.add(first)
            taken.add(second)

    return g

if __name__ == "__main__":    
    # just here for printout
    def printvals(lst: list) -> None:
        for i in range(len(lst)-1):
            print(lst[i].val, end=" -> ")
        if len(lst) > 0:
            print(lst[-1].val)

    graph = DirectedGraph.DirectedGraph()

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


    # REQUIRED ASSIGNMENT TEST CASES BELOW
    rand = createRandomDAGIter(1000)

    printvals(TopSort.TopSort.Kahns(graph))
    printvals(TopSort.TopSort.mDFS(graph))

    printvals(TopSort.TopSort.Kahns(rand))
    printvals(TopSort.TopSort.mDFS(rand))
