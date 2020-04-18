import Node
import Graph

import collections

# Provides topological sort functions for use on a Graph
class TopSort:

    # Performs Kahn's topological sort on a given graph
    @classmethod
    def Kahns(cls, graph: Graph) -> list:
        inDeg = {node:0 for node in graph.getAllNodes()}

        for node in graph.getAllNodes():
            for neighbor in node.neighbors:
                inDeg[neighbor] += 1

        retList = []
        queue = collections.deque()

        for node in inDeg:
            if inDeg[node] == 0:
                queue.append(node)
                inDeg[node] -= 1

        while len(queue) > 0:
            n = queue.popleft()
            retList.append(n)
            for node in n.neighbors:
                inDeg[node] -= 1
                if inDeg[node] == 0:
                    queue.append(node)
            inDeg[n] -= 1

        return retList

    # Performs modified Depth-First-Search on a given Graph to do a topological sort
    @classmethod
    def mDFS(cls, graph: Graph) -> list:
        stack = []
        visited = []

        for node in graph.getAllNodes():
            if not node.getVisited():
                cls.mDFSHelper(node, stack)
        
        return [val for val in reversed(stack)]

    @classmethod
    def mDFSHelper(cls, node: Node, stack: list) -> None:
        node.setVisited()
        for neighbor in node.neighbors:
            if not neighbor.getVisited():
                cls.mDFSHelper(neighbor, stack)
        stack.append(node)