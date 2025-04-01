class arrayDoublyLinkedList:
    def __init__(self):
        self.array = []
    
    def length(self):
        return len(self.array)

    def append(self, element: str):
        self.array.append(element)