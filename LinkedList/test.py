from LinkedList import LinkedList

myList = LinkedList()

# testing empty LinkedList
print(myList, f'Length: {myList.getLen()}')

print('--------------')

# testing append
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)

print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

print('--------------')

# testing insert
myList.insert(10, 0)
myList.insert(6, 3)
myList.insert(5, 7)
myList.insert(15, 100)
myList.insert(-20, -100)

print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

print('--------------')

# testing push/pop
myList = LinkedList()

myList.push(1)
myList.push(2)
myList.push(3)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

print(f'Pop val: {myList.pop()}')
print(f'Pop val: {myList.pop()}')
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

print(f'Pop val: {myList.pop()}')
print(f'Pop val: {myList.pop()}')
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root}', f'end: {myList.end}')

print('--------------')

# testing remove and clear
myList = LinkedList()

myList.push(1)
myList.push(2)
myList.push(3)

myList.remove(2)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.remove(3)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList = LinkedList()

myList.push(1)
myList.push(2)
myList.push(3)

myList.remove(1)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.remove(10)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.clear()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root}', f'end: {myList.end}')

print('--------------')

# testing swap
myList = LinkedList()

myList.push(1)
myList.push(2)
myList.push(3)
myList.push(4)
myList.push(5)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.swap(1, 4)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.swap(3, 0)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

print('--------------')

# testing update
myList = LinkedList()

myList.push(1)
myList.push(2)
myList.push(3)
myList.push(4)
myList.push(5)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.update(3, 10)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.update(9999, 10)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.update(1, 50)
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

print('--------------')

# testing combine
list1 = LinkedList()

list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)

list2 = LinkedList()

list2.push(6)
list2.push(7)
list2.push(8)
list2.push(9)
list2.push(10)

list1.combine(list2)
print(list1, f'Length: {list1.getLen()}')
print(f'start: {list1.root.val}', f'end: {list1.end.val}')

list1 = LinkedList()
list2 = LinkedList()

list1.combine(list2)
print(list1, f'Length: {list1.getLen()}')
print(f'start: {list1.root}', f'end: {list1.end}')

list1 = LinkedList()
list2 = LinkedList()

list1.push(1)
list1.push(2)
list1.push(3)

list1.combine(list2)
print(list1, f'Length: {list1.getLen()}')
print(f'start: {list1.root.val}', f'end: {list1.end.val}')

list1 = LinkedList()
list2 = LinkedList()

list2.push(6)
list2.push(7)
list2.push(8)

list1.combine(list2)
print(list1, f'Length: {list1.getLen()}')
print(f'start: {list1.root.val}', f'end: {list1.end.val}')

print('--------------')

# testing shuffle
myList = LinkedList()

for i in range(10):
    myList.push(i)

print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.shuffle()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList.shuffle()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList = LinkedList()
myList.push(10)
myList.shuffle()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

myList = LinkedList()
myList.shuffle()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root}', f'end: {myList.end}')

print('--------------')

# testing sorting algorithms
myList = LinkedList()

for i in range(10):
    myList.push(i)

myList.shuffle()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')
myList.bubbleSort()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

print()
myList.shuffle()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')
myList.insertionSort()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')

# print()
# myList.shuffle()
# print(myList, f'Length: {myList.getLen()}')
# print(f'start: {myList.root.val}', f'end: {myList.end.val}')
# myList.quickSort()
# print(myList, f'Length: {myList.getLen()}')
# print(f'start: {myList.root.val}', f'end: {myList.end.val}')

# print()
# myList.shuffle()
# print(myList, f'Length: {myList.getLen()}')
# print(f'start: {myList.root.val}', f'end: {myList.end.val}')
# #
# print(myList, f'Length: {myList.getLen()}')
# print(f'start: {myList.root.val}', f'end: {myList.end.val}')

print('--------------')

# testing toList
myList = LinkedList()

for i in range(10):
    myList.push(i)

print(f'to list: {myList.toList()}')

myList.shuffle()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root.val}', f'end: {myList.end.val}')
print(f'to list: {myList.toList()}')

myList = LinkedList()
print(myList, f'Length: {myList.getLen()}')
print(f'start: {myList.root}', f'end: {myList.end}')
print(f'to list: {myList.toList()}')

print('--------------')
