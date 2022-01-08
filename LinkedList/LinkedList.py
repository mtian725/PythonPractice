import random
random.seed(0)

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# top the stack is at index 0
class LinkedList:
    def __init__(self):
        self.root = None
        self.end = None
        self.length = 0
    
    # add to the end of the linked list
    def append(self, val):
        newNode = Node(val, None)
        if self.root:
            self.end.next = newNode
            self.end = self.end.next
        else:
            self.root = newNode
            self.end = newNode
        self.length += 1

    # add to specific index, pushing all values originally from [index, length-1] 
    # to [index + 1, length]
    # the range of inputs is [0, len]
    # if index is out of range, just auto place it to 0 or len
    def insert(self, val, index):
        newNode = Node(val, None)
        if index <= 0:
            newNode.next = self.root
            self.root = newNode
        elif index >= self.length:
            self.end.next = newNode
            self.end = self.end.next
        else:
            count = 1
            curr = self.root
            while curr and count != index:
                curr = curr.next
                count += 1
            newNode.next = curr.next
            curr.next = newNode
        self.length += 1

    # add to the front of the list
    def push(self, val):
        newNode = Node(val, self.root)
        if not self.root:
            self.end = newNode
        self.root = newNode
        self.length += 1

    # remove from front of the list and return it
    def pop(self):
        if self.root:
            out = self.root.val
            self.root = self.root.next
            self.length -= 1
            if not self.root:
                self.end = None
            return out
        else:
            return None

    # remove a specific target, do nothing if val not found
    def remove(self, target):
        curr = self.root
        prev = None
        while curr and curr.val != target:
            prev = curr
            curr = curr.next

        if curr:
            if curr == self.end:
                self.end = prev

            if prev:
                prev.next = curr.next
            else:
                self.root = curr.next
            self.length -= 1

    # reset the entire linked list
    def clear(self):
        self.root = None
        self.end = None
        self.length = 0

    # swap nodes at index i and j
    ## just assume that user will use valid inputs for simplicity sake
    def swap(self, i, j):
        first = min(i, j)
        second = max(i, j)
        
        curr = self.root
        count = 0
        while curr and count != first:
            curr = curr.next
            count += 1

        temp = curr

        while curr and count != second:
            curr = curr.next
            count += 1

        tempVal = curr.val
        curr.val = temp.val
        temp.val = tempVal

    # update the first instance of target with newVal
    # do nothing if target not found
    def update(self, target, newVal):
        curr = self.root
        while curr and curr.val != target:
            curr = curr.next
        
        if curr:
            curr.val = newVal

    # combine two linkedLists together so it's self -> otherList
    def combine(self, otherList):
        if otherList.root:
            if self.root:
                self.end.next = otherList.root
                self.end = otherList.end
            else:
                self.root = otherList.root
                self.end = otherList.end
        self.length += otherList.length

    def getLen(self):
        return self.length

    # fisher-yates shuffling algorithm
    def shuffle(self):
        # note not in place
        newList = None

        count = self.length
        while count:
            r = random.randint(0, count-1)

            curr = self.root
            prev = None
            while r:
                prev = curr
                curr = curr.next
                r -= 1

            if prev:
                prev.next = curr.next
            else:
                self.root = curr.next

            newList = Node(curr.val, newList)
            count -= 1

        # reset end and new list
        self.root = newList
        curr = self.root
        # this works because if curr is null it will short circuit and not throw error
        while curr and curr.next:
            curr = curr.next
        self.end = curr

    def bubbleSort(self):
        for i in range(self.length):
            curr = self.root
            while curr.next:
                if curr.val > curr.next.val:
                    temp = curr.val
                    curr.val = curr.next.val
                    curr.next.val = temp
                curr = curr.next

    def insertionSort(self):
        # note, is not in place
        newList = None
        while self.root:
            curr = newList
            prev = None
            while curr and self.root.val > curr.val:
                prev = curr
                curr = curr.next
            
            if not prev:
                newList = Node(self.root.val, newList)
            else:
                prev.next = Node(self.root.val, curr)

            self.root = self.root.next
        self.root = newList
        curr = self.root
        # this works because if curr is null it will short circuit and not throw error
        while curr and curr.next:
            curr = curr.next
        self.end = curr

    # def quickSort(self):
    #     self.quickSortHelper(self.root, 0, self.length)

    # def quickSortHelper(self, ll, lo, hi):
    #     if lo < hi:
    #         part = self.partition(ll, lo, hi)

    #         # self.quickSortHelper(ll, lo, part - 1)
    #         # self.quickSortHelper(ll, part + 1, hi)

    # def partition(self, ll, lo, hi):
    #     # gunna use first element as the pivot
    #     pivot_val = ll.val
    #     i = lo - 1

    #     curr = ll
    #     count = lo 
    #     while count:
    #         curr = curr.next
    #         count -= 1

    #     for k in range(lo, hi):
    #         print(curr.val, self.toList())
    #         if curr.val < pivot
    #             i += 1

    #         curr = curr.next
        
    #     print(self.toList())

    #     return -1


    # def mergeSort(self):

    def toList(self):
        arr = []
        curr = self.root
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def __str__(self):
        out = 'LinkedList: '
        curr = self.root
        if curr:
            while curr.next:
                out += f'{curr.val} -> '
                curr = curr.next

            out += f'{curr.val}'
        else:
            out += 'EMPTY'

        return out.format(self=self)