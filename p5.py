import random
import NodeW
import WeightedGraph

def createRandomCompleteWeightedGraph(n: int) -> WeightedGraph:
    wGraph = WeightedGraph.WeightedGraph()
    for i in range(n):
        wGraph.addNode(i)
    for node in wGraph.getAllNodes():
        for node2 in wGraph.getAllNodes():
            if node != node2:
                wGraph.addWeightedEdge(node, node2, random.randint(1,100))
    return wGraph

def createLinkedList(n: int) -> WeightedGraph:
    g = WeightedGraph.WeightedGraph()
    g.addNode(0)
    for i in range(1, n):
        g.addNode(i)
        g.addWeightedEdge(g.nodes[i-1], g.nodes[i], 1)
    return g

def minDistance(d: dict, visited: set) -> NodeW:
    ans = None
    m = float('inf')
    for node in d:
        if node not in visited and d[node] <= m:
            m = d[node]
            ans = node
    return ans

def dijkstras(start: NodeW) -> dict:
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
    sampleLinkedList = createLinkedList(100)

    graph = WeightedGraph.WeightedGraph()

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

    graph.addWeightedEdge(graph.nodes[3], graph.nodes[5], 1)
    graph.addWeightedEdge(graph.nodes[5], graph.nodes[3], 1)

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

    graph.addWeightedEdge(graph.nodes[4], graph.nodes[6], 4)
    graph.addWeightedEdge(graph.nodes[6], graph.nodes[4], 4)

    testdijkstras = dijkstras(graph.nodes[0])
    for key in testdijkstras:
        print('{}: {}'.format(key.val, testdijkstras[key]))

    epicgraph = createRandomCompleteWeightedGraph(100)
    epicdijkstras = dijkstras(epicgraph.nodes[0])
    for key in epicdijkstras:
        print('{}: {}'.format(key.val, epicdijkstras[key]))