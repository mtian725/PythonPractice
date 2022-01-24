
from inspect import stack
from os import path
from pickletools import stackslice


def TopologicalSort(graph):

    paths = []
    visited = [False] * len(graph)

    for i in range(len(graph)):
        temp_path = []
        stack = [i]
        while stack:
            val = stack.pop(0)
            if not visited[val]:
                stack += graph[val]
                visited[val] = True
                temp_path.append(val)

        temp_path.reverse()
        paths += temp_path

    paths.reverse()
    return paths