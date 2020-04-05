import p6
import p5

def minDistance(d, visited):
    ans = None
    m = float('inf')
    for node in d:
        if node not in visited and d[node] <= m:
            m = d[node]
            ans = node
    return ans

def countingDijkstras(start):
    d = {}
    d[start] = 0
    visited = set()

    vCount = 0
    while start and start in d:
        visited.add(start)
        vCount += 1
        for neighbor in start.neighbors:
            if neighbor not in visited:
                newD = d[start] + start.weights[neighbor]
                if neighbor not in d or newD < d[neighbor]:
                    d[neighbor] = newD
        start = minDistance(d, visited)

    print("Dijkstra's nodes that are visited:", vCount, "%")
    return d

def manhattanDistance(node, destNode):
    return abs(node.x - destNode.x) + abs(node.y - destNode.y)
    
def minDistance2(d, visited):
    ans = None
    m = float('inf')
    for node in d:
        if node not in visited and d[node][0] + d[node][1] <= m:
            m = d[node][0] + d[node][1]
            ans = node
    return ans   

def countingAstar(sourceNode, destNode):
    d = {}
    d[sourceNode] = (0, manhattanDistance(sourceNode, destNode), None)
    curr = sourceNode
    visited = set()

    vCount = 0
    while curr and curr != destNode:
        visited.add(curr)
        vCount += 1
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                newD = d[curr][0]
                h = manhattanDistance(neighbor, destNode)
                if neighbor not in d or newD + h < d[neighbor][0] + d[neighbor][1]:
                    d[neighbor] = (newD, h, curr)
        curr = minDistance2(d, visited)

    path = destNode
    traversal = []
    while path:
        traversal.insert(0, path)
        if path in d:
            path = d[path][2]
        else:
            print("A* nodes that are visited:", round(vCount/10000*100, 2), "%")
            return [] # means no path to goal

    print("A* nodes that are visited:", round(vCount/10000*100, 2), "%")
    return traversal

g5 = p5.createRandomCompleteWeightedGraph(100)
countingDijkstras(g5.nodes[0])

g6 = p6.createRandomGridGraph(100)
sourceNode = g6.nodes[(0, 0)]
destNode = g6.nodes[(99, 99)]
countingAstar(sourceNode, destNode)