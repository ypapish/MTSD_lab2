import unittest
from arrDoublyLinkedList import arrayDoublyLinkedList


class TestArrayDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.List = arrayDoublyLinkedList()

    def test_length(self):
        self.assertEqual(self.List.length(), 0)