import unittest
from arrDoublyLinkedList import arrayDoublyLinkedList


class TestArrayDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.List = arrayDoublyLinkedList()

    def test_length(self):
        self.assertEqual(self.List.length(), 0)
    
    def test_append(self):
        self.List.append('A')
        self.assertEqual(self.List.length(), 1)
        self.assertEqual(self.List.get(0), 'A')

        self.List.append('B')
        self.assertEqual(self.List.length(), 2)
        self.assertEqual(self.List.get(1), 'B')

    def test_insert(self):
        self.List.insert('A', 0)
        self.assertEqual(self.List.get(0), 'A')

        self.List.insert('B', 0)
        self.assertEqual(self.List.get(0), 'B')
        self.assertEqual(self.List.get(1), 'A')

        self.List.insert('C', 2)
        self.assertEqual(self.List.get(2), 'C')

        self.List.insert('D', 1)
        self.assertEqual(self.List.get(1), 'D')

        with self.assertRaises(IndexError):
            self.List.insert('E', -1)
        with self.assertRaises(IndexError):
            self.List.insert('E', 5)