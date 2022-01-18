from MaxHeap import MaxHeap

heap = MaxHeap([])

print(heap)

heap.add(1)
heap.add(2)
heap.add(3)
heap.add(4)
heap.add(5)
heap.add(6)
heap.add(7)

print(heap)

print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())

heap = MaxHeap([52, 27, 33, 86, 49, 55, 23, 89, 19, 18])

print(heap)
