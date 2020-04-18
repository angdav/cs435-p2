import Node

class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, val: int) -> None:
        node = Node.Node(val)
        self.nodes.append(node)

    def addUndirectedEdge(self, first: Node, second: Node) -> None:
        first.neighbors.add(second)
        second.neighbors.add(first)
    
    def removeUndirectedEdge(self, first: Node, second: Node) -> None:
        first.neighbors.discard(second)
        second.neighbors.discard(first)

    def getAllNodes(self) -> set:
        return set(self.nodes)