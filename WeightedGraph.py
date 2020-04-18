import Graph
import NodeW

class WeightedGraph(Graph.Graph):

    def addNode(self, val: int) -> None:
        node = NodeW.NodeW(val)
        self.nodes.append(node)

    def addWeightedEdge(self, first: NodeW, second: NodeW, edgeWeight: int) -> None:
        if second not in first.neighbors:
            first.neighbors.add(second)
            first.weights[second] = edgeWeight
    
    def removeWeightedEdge(self, first: NodeW, second: NodeW) -> None:
        if second in first.neighbors:
            first.neighbors.remove(second)
            del first.weights[second]