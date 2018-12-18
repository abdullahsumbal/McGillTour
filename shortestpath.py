import json
import sys
class Node:
    def __init__(self, name , coordinate):
        self.name = name
        self.coordinate = coordinate
        self.adj = {}
        self.previous = None
        self.shortest_distance_from_source = sys.maxsize

    def addDestination(self, node, distance):
        self.adj[node] = distance

class Graph:
    def __init__(self):
        self.graph = []

    def addNode(self, node):
        self.graph.append(node)

    def dijkstra(self, node):
        return 1
if __name__ == '__main__':
    with open('edges.json') as f:
        data = json.load(f)

    nodes = {}
    for name, coordinate in data["Points"].items():
        nodes[name] = Node(name, coordinate)

    for name, adjNodes in data["Edges"].items():
        for adjNode in adjNodes:
            nodes[name].addDestination(nodes[adjNode], 2)

    graph = Graph()
    for _,node in nodes.items():
        graph.addNode(node)
