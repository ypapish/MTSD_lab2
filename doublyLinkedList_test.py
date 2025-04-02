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
            self.List.insert('E', 7)

    def test_delete(self):
        self.List.append('A')
        self.List.append('B')
        self.List.append('C')

        self.assertEqual(self.List.delete(1), 'B')
        self.assertEqual(self.List.length(), 2)

        self.assertEqual(self.List.delete(0), 'A')
        self.assertEqual(self.List.length(), 1)

        self.assertEqual(self.List.delete(0), 'C')
        self.assertEqual(self.List.length(), 0)

        with self.assertRaises(IndexError):
            self.List.delete(-1)
        with self.assertRaises(IndexError):
            self.List.delete(0)
    
    def test_deleteAll(self):
        self.List.append('A')
        self.List.append('B')
        self.List.append('A')
        self.List.append('C')
        self.List.append('A')

        self.List.deleteAll('A')
        self.assertEqual(self.List.length(), 2)
        self.assertEqual(self.List.get(0), 'B')
        self.assertEqual(self.List.get(1), 'C')

        self.List.deleteAll('X')
        self.assertEqual(self.List.length(), 2)