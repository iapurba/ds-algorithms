#!/usr/bin/env python3

# DFS graph searching algorithm 
# using our own stack
def dfs(graph, start):

    stack = []
    visited = set()

    # Add start to the search
    stack.append(start)

    while len(stack):
        # Pull a node
        current = stack.pop()

        # Process if not in visited
        if current not in visited:
            visited.add(current)
            print(current)

        # Add unvisited children to the stack
        for child in graph[current]:
            if child not in visited:
                stack.append(child)


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

    dfs(graph, 'C')
