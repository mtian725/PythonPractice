
from cgitb import small
from cmath import cos
from inspect import stack
import math
from pickletools import stackslice
from turtle import st


def DijkstraAlg(graph, start, end):
    max_nodes = len(graph)

    visited = set()
    
    path = [None] * max_nodes
    cost = [0] * max_nodes

    for i in range(max_nodes):
        if i != start:
            cost[i] = math.inf

    while True:
        smallest_k = -1
        for k in range(0, max_nodes):
            if k not in visited:
                if smallest_k == -1:
                    smallest_k = k
                elif cost[k] < cost[smallest_k]:
                    smallest_k = k
                
        if smallest_k == -1:
            break

        visited.add(smallest_k)

        for i in range(max_nodes):
            if graph[smallest_k][i] and i not in visited:
                if cost[smallest_k] + graph[smallest_k][i] < cost[i]:
                    cost[i] = cost[smallest_k] + graph[smallest_k][i]
                    path[i] = smallest_k

    if path[end] != None:
        solu = [end]
        curr = end
        while curr != start:
            curr = path[curr]
            solu.append(curr)
        solu.reverse()
        print(solu)
    else:
        print(path, cost, path[end])
        print(f'No path from {start} to {end}')
    return