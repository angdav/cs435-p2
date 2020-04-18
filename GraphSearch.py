import Node
import Graph

# Provides traversal and search functions for Graphs
class GraphSearch:
    
    # Performs a Depth-First-Search recursively on a given starting node and ending node
    @classmethod
    def DFSRec(cls, start: Node, end: Node) -> list:
        return cls.DFSRecHelper(start, end, {start}, [start], [])

    @classmethod
    def DFSRecHelper(cls, start: Node, end: Node, visited: set, stack: list, traversal: list) -> list:
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
        return None

    # Performs a Depth-First-Search iteratively on a given starting node and ending node
    @classmethod
    def DFSIter(cls, start: Node, end: Node):
        visited = set()
        stack = [start]
        visited.add(start)
        traversal = []

        while len(stack) > 0:
            curr = stack.pop()
            traversal.append(curr)
            if curr == end:
                return traversal
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return None

    # Performs a Breadth-First-Search iteratively on a given Graph
    @classmethod
    def BFTIter(cls, graph: Graph):
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
    
    # Performs a Breadth-First-Search recursively on a given Graph
    @classmethod
    def BFTRec(cls, graph: Graph):
        return cls.BFTRecHelper(graph, set(), [], [])

    @classmethod
    def BFTRecHelper(cls, graph: Graph, visited: set, queue: list, traversal: list):
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