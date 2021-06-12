#!/usr/bin/env python3

class Graph:

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size


    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"{v1} and {v2} are same, can not connect vertex to itself")
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1


    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print(f"No commection between {v1} and {v2}")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    # Print the adjacency matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)


if __name__ == "__main__":

    g = Graph(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)

    g.print_matrix()
