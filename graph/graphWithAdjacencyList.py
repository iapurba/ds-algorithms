#!/usr/bin/env python3

# Graph implementation using adjacency list
class Graph:
    def __init__(self):
        self.graph = {}
        self.size = 0

    def add_vertex(self, v):
        self.graph[v] = []
        self.size += 1


    def add_edge(self, v1, v2):
        # As this is an undirected graph we must connect two nodes,
        # and other way around
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
        return self


    # Helper function to print the graph representation
    def print_graph(self):
        for key, value in self.graph.items():
            print(str(key) + " --> ", end="")
            if value:
                print(value, end="")
            print()


if __name__ == "__main__":
    g = Graph()

    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)

    g.print_graph()
