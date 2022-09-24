"""
The abstract types - Unit tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Functions to test the abstract linear data types of lists, stacks and queues implemented in Python
"""

__author__ = "RobiPoire"

import unittest
from abstract_types import *


class TestLists(unittest.TestCase):

    def test_list_creation(self):
        """Test the creation of a list"""
        list = Lists(5)
        self.assertEqual(list.size, 5)
        self.assertEqual(list.list, [0, 0, 0, 0, 0, 0])

    def test_list_insert(self):
        """Test the insertion of an element in a list"""
        list = Lists(5)
        list.insert("Hello", 1)
        self.assertEqual(list.list, [1, "Hello", 0, 0, 0, 0])
        list.insert("World", 2)
        self.assertEqual(list.list, [2, "Hello", "World", 0, 0, 0])
        list.insert("!", 3)
        self.assertEqual(list.list, [3, "Hello", "World", "!", 0, 0])

    def test_list_delete(self):
        """Test the deletion of an element in a list"""
        list = Lists(5)
        list.insert("Hello", 1)
        list.insert("World", 2)
        list.insert("!", 3)
        list.delete(1)
        self.assertEqual(list.list, [2, "World", "!", 0, 0, 0])
        list.delete(2)
        self.assertEqual(list.list, [1, 'World', 0, 0, 0, 0])
        list.delete(1)
        self.assertEqual(list.list, [0, 0, 0, 0, 0, 0])

    def test_list_full(self):
        """Test the fullness of a list"""
        list = Lists(5)
        self.assertEqual(list.is_full(), False)
        list.insert("Hello", 1)
        list.insert("World", 2)
        list.insert("!", 3)
        list.insert("Hello", 4)
        list.insert("World", 5)
        self.assertEqual(list.is_full(), True)

    def test_list_empty(self):
        """Test the emptiness of a list"""
        list = Lists(5)
        self.assertEqual(list.is_empty(), True)
        list.insert("Hello", 1)
        list.insert("World", 2)
        list.insert("!", 3)
        list.insert("Hello", 4)
        list.insert("World", 5)
        self.assertEqual(list.is_empty(), False)

    def test_list_search(self):
        """Test the search of an element in a list"""
        list = Lists(5)
        list.insert("Hello", 1)
        list.insert("World", 2)
        list.insert("!", 3)
        self.assertEqual(list.search("Hello"), 1)
        self.assertEqual(list.search("World"), 2)
        self.assertEqual(list.search("!"), 3)
        # Si l'élément n'est pas dans la liste retourne bien une erreur
        with self.assertRaises(ValueError):
            list.search("Test")


class TestStacks(unittest.TestCase):

    def test_stack_creation(self):
        """Test the creation of a stack"""
        stack = Stacks(5)
        self.assertEqual(stack.size, 5)
        self.assertEqual(stack.stack, [1, 0, 0, 0, 0, 0])

    def test_stack_add(self):
        """Test the addition of an element in a stack"""
        stack = Stacks(5)
        stack.add("Hello")
        self.assertEqual(stack.stack, [2, "Hello", 0, 0, 0, 0])
        stack.add("World")
        self.assertEqual(stack.stack, [3, "Hello", "World", 0, 0, 0])
        stack.add("!")
        self.assertEqual(stack.stack, [4, "Hello", "World", "!", 0, 0])

    def test_stack_retrieve(self):
        """Test the retrieval of an element in a stack"""
        stack = Stacks(5)
        stack.add("Hello")
        stack.add("World")
        stack.add("!")
        stack.retrieve()
        self.assertEqual(stack.stack, [3, 'Hello', 'World', '!', 0, 0])
        stack.retrieve()
        self.assertEqual(stack.stack, [2, 'Hello', 'World', '!', 0, 0])
        stack.retrieve()
        self.assertEqual(stack.stack, [1, 'Hello', 'World', '!', 0, 0])

    def test_stack_full(self):
        """Test the fullness of a stack"""
        stack = Stacks(5)
        self.assertEqual(stack.is_full(), False)
        stack.add("Hello")
        stack.add("World")
        stack.add("!")
        stack.add("Hello")
        stack.add("World")
        self.assertEqual(stack.is_full(), True)

    def test_stack_empty(self):
        """Test the emptiness of a stack"""
        stack = Stacks(5)
        self.assertEqual(stack.is_empty(), True)
        stack.add("Hello")
        stack.add("World")
        stack.add("!")
        stack.add("Hello")
        stack.add("World")
        self.assertEqual(stack.is_empty(), False)


class TestQueues(unittest.TestCase):

    def test_queue_creation(self):
        """Test the creation of a queue"""
        queue = Queues(5)
        self.assertEqual(queue.size, 5)
        self.assertEqual(queue.queue, [3, 3, 0, 0, 0, 0, 0, 0])

    def test_queue_put(self):
        """Test the addition of an element in a queue"""
        queue = Queues(5)
        queue.put("Hello")
        self.assertEqual(queue.queue, [3, 4, 1, "Hello", 0, 0, 0, 0])
        queue.put("World")
        self.assertEqual(queue.queue, [3, 5, 2, "Hello", "World", 0, 0, 0])
        queue.put("!")
        self.assertEqual(queue.queue, [3, 6, 3, "Hello", "World", "!", 0, 0])

    def test_queue_get(self):
        """Test the retrieval of an element in a queue"""
        queue = Queues(5)
        queue.put("Hello")
        queue.put("World")
        queue.put("!")
        queue.get()
        self.assertEqual(queue.queue, [4, 6, 2, 'Hello', 'World', '!', 0, 0])
        queue.get()
        self.assertEqual(queue.queue, [5, 6, 1, 'Hello', 'World', '!', 0, 0])
        queue.get()
        self.assertEqual(queue.queue, [6, 6, 0, 'Hello', 'World', '!', 0, 0])

    def test_queue_full(self):
        """Test the fullness of a queue"""
        queue = Queues(5)
        self.assertEqual(queue.is_full(), False)
        queue.put("Hello")
        queue.put("World")
        queue.put("!")
        queue.put("Hello")
        queue.put("World")
        self.assertEqual(queue.is_full(), True)

    def test_queue_empty(self):
        """Test the emptiness of a queue"""
        queue = Queues(5)
        self.assertEqual(queue.is_empty(), True)
        queue.put("Hello")
        queue.put("World")
        queue.put("!")
        queue.put("Hello")
        queue.put("World")
        self.assertEqual(queue.is_empty(), False)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
