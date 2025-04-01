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