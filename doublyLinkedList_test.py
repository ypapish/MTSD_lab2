import unittest
from doublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.List = DoublyLinkedList()

    def test_length(self):
        self.assertEqual(self.List.length(), 0)

    def test_append(self):
        self.List.append('A')
        self.assertEqual(self.List.length(), 1)
        self.assertEqual(self.List.get(0), 'A')

        self.List.append('B')
        self.assertEqual(self.List.length(), 2)
        self.assertEqual(self.List.get(1), 'B')
