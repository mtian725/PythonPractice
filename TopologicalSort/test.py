
from TopologicalSort import TopologicalSort

def test1():
    graph.append([])
    graph.append([])
    graph.append([3])
    graph.append([1])
    graph.append([0,1])
    graph.append([0,2])

def test2():
    graph.append([1,2])
    graph.append([3,4])
    graph.append([3,5])
    graph.append([4,5])
    graph.append([])
    graph.append([])

def test3():
    graph.append([])
    graph.append([3,4])
    graph.append([3,5])
    graph.append([4,5])
    graph.append([])
    graph.append([])

def printGraph():
    for i in range(len(graph)):
        print(f'{i} : {graph[i]}')

graph = []
test1()
printGraph()
sol = TopologicalSort(graph)
print(sol)
print("===================")

graph = []
test2()
printGraph()
sol = TopologicalSort(graph)
print(sol)
print("===================")

graph = []
test3()
printGraph()
sol = TopologicalSort(graph)
print(sol)
print("===================")

