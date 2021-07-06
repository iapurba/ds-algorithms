#!/usr/bin/env python3

# BFS graph searching algorithm
def bfs(graph, start):

    # Although time complexity of poping the first element out
    # from an array (linear: O(n)) is not same as dequeue (constant O(1)),
    # we pretending a queue by using an array here
    queue = []
    visited = set()

    # Add start to the search
    queue.append(start)

    while len(queue):
        # Pull a node
        current = queue.pop(0)

        # Process if not visited
        if current not in visited:
            visited.add(current)
            print(current)

        # Add unvisited children to the queue
        for child in graph[current]:
            if child not in visited:
                queue.append(child)


if __name__ == "__main__":

    graph = {
        'A': set(['B', 'G']),
        'B': set(['A', 'C', 'D']),
        'C': set(['B', 'D', 'E', 'F']),
        'D': set(['B', 'C', 'E']),
        'E': set(['C', 'D', 'F', 'H']),
        'F': set(['C', 'E', 'G']),
        'G': set(['A', 'F', 'H']),
        'H': set(['E', 'G']),
    }

    bfs(graph, 'C')
