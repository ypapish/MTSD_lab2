class Node:
    def __init__(self, value: str):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def length(self):
        return self.size

    def append(self, element: str):
        newNode = Node(element)
        if not self.head:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

    def insert(self, element: str, index: int):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        newNode = Node(element)
        if index == 0:
            newNode.next = self.head
            if self.head:
                self.head.prev = newNode
            self.head = newNode
            if self.size == 0:
                self.tail = newNode
        elif index == self.size:
            self.append(element)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            newNode.next = current
            newNode.prev = current.prev
            current.prev.next = newNode
            current.prev = newNode
        self.size += 1

    def delete(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            removedValue = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.size - 1:
            removedValue = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            removedValue = current.value
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1
        return removedValue
