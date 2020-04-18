import Graph
import NodeV

class DirectedGraph(Graph.Graph):

    def addNode(self, val: int) -> None:
        node = NodeV.NodeV(val)
        self.nodes.append(node)

    def addDirectedEdge(self, first: NodeV, second: NodeV) -> None:
        if second not in first.neighbors:
            first.neighbors.add(second)
    
    def removeDirectedEdge(self, first: NodeV, second: NodeV) -> None:
        if second in first.neighbors:
            first.neighbors.remove(second)