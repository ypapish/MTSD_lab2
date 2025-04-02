import unittest
from doublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.List = DoublyLinkedList()

    def test_length(self):
        self.assertEqual(self.List.length(), 0)
