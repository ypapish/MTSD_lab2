class arrayDoublyLinkedList:
    def __init__(self):
        self.array = []
    
    def length(self):
        return len(self.array)

    def append(self, element: str):
        self.array.append(element)

    def insert(self, element: str, index: int):
        if index < 0 or index > len(self.array):
            raise IndexError("Index out of range")
        self.array.insert(index, element)
    
    def delete(self, index: int):
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        return self.array.pop(index)

    def deleteAll(self, element: str):
        self.array = [elem for elem in self.array if elem != element]

    def get(self, index: int):
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        return self.array[index]

    def clone(self):
        newDoubleLinkedList = arrayDoublyLinkedList()
        newDoubleLinkedList.array = self.array.copy()
        return newDoubleLinkedList

    def reverse(self):
        self.array.reverse()

    def findFirst(self, element: str) -> int:
        try:
            return self.array.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str):
        for index in range(len(self.array)-1, -1, -1):
            if self.array[index] == element:
                return index
        return -1

    def clear(self):
        self.array.clear()