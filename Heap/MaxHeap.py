
class MaxHeap:
    def __init__(self, arr):
        self.heap = self.heapify(arr)

    def heapify(self, arr):
        def heapify_helper(arr, index, size):
            leftC   = 2*index + 1
            rightC  = 2*index + 2
            max_index = index
            if leftC < size and arr[leftC] > arr[max_index]:
                max_index = leftC

            if rightC < size and arr[rightC] > arr[max_index]:
                max_index = rightC

            if max_index != index:
                arr[max_index], arr[index] = arr[index], arr[max_index]
                heapify_helper(arr, max_index, size)

        last_non_leaf_node = len(arr) // 2 - 1
        for i in range(last_non_leaf_node, -1, -1):
            heapify_helper(arr, i, len(arr))
        return arr

    def add(self, val):
        self.heap.append(val)
        self.heap = self.heapify(self.heap)

    def pop(self):
        val = self.heap.pop(0)
        self.heap = self.heapify(self.heap)
        return val        

    def __str__(self):
        arr = ','.join(str(v) for v in self.heap)
        return f'[{arr}]'.format(self=self)