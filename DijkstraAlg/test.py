
from DijkstraAlg import DijkstraAlg
import random


random.seed(1)

graph = []
for i in range(10):
    graph.append([0] * 10)

def printGraph():
    for edges in graph:
        print(edges)

def generateRandomGraph():
    for i in range(10):
        for j in range(i, min(i+5,10)):
            if i != j:
                graph[i][j] = random.randint(1,10)
                graph[j][i] = graph[i][j]

def test1():
    graph[0][1] = 5
    graph[1][0] = 5
    graph[0][2] = 8
    graph[2][0] = 8
    graph[1][2] = 1
    graph[2][1] = 1
    graph[1][3] = 10
    graph[3][1] = 10
    graph[2][3] = 3
    graph[3][2] = 3
    graph[3][4] = 9
    graph[4][3] = 9

test1()
printGraph()
DijkstraAlg(graph, 0, 4)
print("-----------------------")

generateRandomGraph()
printGraph()
DijkstraAlg(graph, 0, 9)
