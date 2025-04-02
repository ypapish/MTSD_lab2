import unittest
from arrDoublyLinkedList import ArrayDoublyLinkedList


class TestArrayDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.List = ArrayDoublyLinkedList()

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

    def test_get(self):
        self.List.append('A')
        self.List.append('B')

        self.assertEqual(self.List.get(0), 'A')
        self.assertEqual(self.List.get(1), 'B')

        with self.assertRaises(IndexError):
            self.List.get(-1)
        with self.assertRaises(IndexError):
            self.List.get(2)

    def test_clone(self):
        self.List.append('A')
        self.List.append('B')

        Clone = self.List.clone()
        self.assertEqual(Clone.length(), 2)
        self.assertEqual(Clone.get(0), 'A')
        self.assertEqual(Clone.get(1), 'B')

        Clone.append('C')
        self.assertEqual(Clone.length(), 3)
        self.assertEqual(self.List.length(), 2)

    def test_reverse(self):
        self.List.append('A')
        self.List.append('B')
        self.List.append('C')

        self.List.reverse()
        self.assertEqual(self.List.get(0), 'C')
        self.assertEqual(self.List.get(1), 'B')
        self.assertEqual(self.List.get(2), 'A')

        Empty = ArrayDoublyLinkedList()
        Empty.reverse()

    def test_findFirst(self):
        self.List.append('A')
        self.List.append('B')
        self.List.append('A')
        self.List.append('C')

    def test_findLast(self):
        self.List.append('A')
        self.List.append('B')
        self.List.append('A')
        self.List.append('C')

        self.assertEqual(self.List.findLast('A'), 2)
        self.assertEqual(self.List.findLast('B'), 1)
        self.assertEqual(self.List.findLast('C'), 3)
        self.assertEqual(self.List.findLast('X'), -1)

    def test_clear(self):
        self.List.append('A')
        self.List.append('B')
        self.List.clear()
        self.assertEqual(self.List.length(), 0)

    def test_extend(self):
        self.List.append('A')
        self.List.append('B')

        Other = ArrayDoublyLinkedList()
        Other.append('C')
        Other.append('D')

        self.List.extend(Other)
        self.assertEqual(self.List.length(), 4)
        self.assertEqual(self.List.get(2), 'C')
        self.assertEqual(self.List.get(3), 'D')

if __name__ == '__main__':
    unittest.main()
