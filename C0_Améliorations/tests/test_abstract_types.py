"""
The abstract types - Unit tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Functions to test the abstract linear data types of lists, stacks and queues implemented in Python
"""

__author__ = "RobiPoire"

import unittest
import sys

sys.path.append("C0_Améliorations/")
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
        self.assertEqual(list.list, [1, "World", 0, 0, 0, 0])
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
        self.assertEqual(list.search("Test"), None)


class TestStacks(unittest.TestCase):
    def test_stack_creation(self):
        """Test the creation of a stack"""
        stack = Stacks(5)
        self.assertEqual(stack.size, 5)
        self.assertEqual(stack.stack, [1, 0, 0, 0, 0, 0])

    def test_stack_push(self):
        """Test the addition of an element in a stack"""
        stack = Stacks(5)
        stack.push("Hello")
        self.assertEqual(stack.stack, [2, "Hello", 0, 0, 0, 0])
        stack.push("World")
        self.assertEqual(stack.stack, [3, "Hello", "World", 0, 0, 0])
        stack.push("!")
        self.assertEqual(stack.stack, [4, "Hello", "World", "!", 0, 0])

    def test_stack_pop(self):
        """Test the retrieval of an element in a stack"""
        stack = Stacks(5)
        stack.push("Hello")
        stack.push("World")
        stack.push("!")
        stack.pop()
        self.assertEqual(stack.stack, [3, "Hello", "World", "!", 0, 0])
        stack.pop()
        self.assertEqual(stack.stack, [2, "Hello", "World", "!", 0, 0])
        stack.pop()
        self.assertEqual(stack.stack, [1, "Hello", "World", "!", 0, 0])

    def test_stack_full(self):
        """Test the fullness of a stack"""
        stack = Stacks(5)
        self.assertEqual(stack.is_full(), False)
        stack.push("Hello")
        stack.push("World")
        stack.push("!")
        stack.push("Hello")
        stack.push("World")
        self.assertEqual(stack.is_full(), True)

    def test_stack_empty(self):
        """Test the emptiness of a stack"""
        stack = Stacks(5)
        self.assertEqual(stack.is_empty(), True)
        stack.push("Hello")
        stack.push("World")
        stack.push("!")
        stack.push("Hello")
        stack.push("World")
        self.assertEqual(stack.is_empty(), False)


class TestQueues(unittest.TestCase):
    def test_queue_creation(self):
        """Test the creation of a queue"""
        queue = Queues(5)
        self.assertEqual(queue.size, 5)
        self.assertEqual(queue.queue, [3, 3, 0, 0, 0, 0, 0, 0])

    def test_queue_enqueue(self):
        """Test the addition of an element in a queue"""
        queue = Queues(5)
        queue.enqueue("Hello")
        self.assertEqual(queue.queue, [3, 4, 1, "Hello", 0, 0, 0, 0])
        queue.enqueue("World")
        self.assertEqual(queue.queue, [3, 5, 2, "Hello", "World", 0, 0, 0])
        queue.enqueue("!")
        self.assertEqual(queue.queue, [3, 6, 3, "Hello", "World", "!", 0, 0])

    def test_queue_dequeue(self):
        """Test the retrieval of an element in a queue"""
        queue = Queues(5)
        queue.enqueue("Hello")
        queue.enqueue("World")
        queue.enqueue("!")
        queue.dequeue()
        self.assertEqual(queue.queue, [4, 6, 2, "Hello", "World", "!", 0, 0])
        queue.dequeue()
        self.assertEqual(queue.queue, [5, 6, 1, "Hello", "World", "!", 0, 0])
        queue.dequeue()
        self.assertEqual(queue.queue, [6, 6, 0, "Hello", "World", "!", 0, 0])

    def test_queue_full(self):
        """Test the fullness of a queue"""
        queue = Queues(5)
        self.assertEqual(queue.is_full(), False)
        queue.enqueue("Hello")
        queue.enqueue("World")
        queue.enqueue("!")
        queue.enqueue("Hello")
        queue.enqueue("World")
        self.assertEqual(queue.is_full(), True)

    def test_queue_empty(self):
        """Test the emptiness of a queue"""
        queue = Queues(5)
        self.assertEqual(queue.is_empty(), True)
        queue.enqueue("Hello")
        queue.enqueue("World")
        queue.enqueue("!")
        queue.enqueue("Hello")
        queue.enqueue("World")
        self.assertEqual(queue.is_empty(), False)


class TestDictionaries(unittest.TestCase):
    def test_dictionary_creation(self):
        """Test the creation of a dictionary"""
        dictionary = Dictionaries(5)
        self.assertEqual(dictionary.size, 5)
        self.assertEqual(dictionary.dictionary, ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))

    def test_dictionary_insert(self):
        """Test the insertion of an element in a dictionary"""
        dictionary = Dictionaries(5)
        dictionary.insert("Hello", 1)
        self.assertEqual(
            dictionary.dictionary, (["Hello", 0, 0, 0, 0], [1, 0, 0, 0, 0])
        )
        dictionary.insert("World", 2)
        self.assertEqual(
            dictionary.dictionary, (["Hello", "World", 0, 0, 0], [1, 2, 0, 0, 0])
        )
        dictionary.insert("!", 3)
        self.assertEqual(
            dictionary.dictionary, (["Hello", "World", 0, "!", 0], [1, 2, 0, 3, 0])
        )

    def test_dictionary_delete(self):
        """Test the deletion of an element in a dictionary"""
        dictionary = Dictionaries(5)
        dictionary.insert("Hello", 1)
        dictionary.insert("World", 2)
        dictionary.insert("!", 3)
        dictionary.delete("Hello")
        self.assertEqual(
            dictionary.dictionary, ([0, "World", 0, "!", 0], [0, 2, 0, 3, 0])
        )
        dictionary.delete("!")
        self.assertEqual(
            dictionary.dictionary, ([0, "World", 0, 0, 0], [0, 2, 0, 0, 0])
        )
        dictionary.delete("World")
        self.assertEqual(dictionary.dictionary, ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))

    def test_dictionary_full(self):
        """Test the fullness of a dictionary"""
        dictionary = Dictionaries(5)
        self.assertEqual(dictionary.is_full(), False)
        dictionary.insert("Hello", 1)
        dictionary.insert("World", 2)
        dictionary.insert("!", 3)
        dictionary.insert("Hello", 4)
        dictionary.insert("World", 5)
        self.assertEqual(dictionary.is_full(), True)

    def test_dictionary_empty(self):
        """Test the emptiness of a dictionary"""
        dictionary = Dictionaries(5)
        self.assertEqual(dictionary.is_empty(), True)
        dictionary.insert("Hello", 1)
        dictionary.insert("World", 2)
        dictionary.insert("!", 3)
        dictionary.insert("Hello", 4)
        dictionary.insert("World", 5)
        self.assertEqual(dictionary.is_empty(), False)

    def test_dictionary_research(self):
        """Test the search of an element in a dictionary"""
        dictionary = Dictionaries(5)
        dictionary.insert("Hello", 1)
        dictionary.insert("World", 2)
        dictionary.insert("!", 3)
        self.assertEqual(dictionary.research(1), "Hello")
        self.assertEqual(dictionary.research(2), "World")
        self.assertEqual(dictionary.research(3), "!")
        self.assertEqual(dictionary.research(4), None)

    def test_dictionary_edit(self):
        """Test the edit of an element in a dictionary"""
        dictionary = Dictionaries(5)
        dictionary.insert("Hello", 1)
        dictionary.insert("World", 2)
        dictionary.insert("!", 3)
        self.assertEqual(
            dictionary.dictionary, (["Hello", "World", 0, "!", 0], [1, 2, 0, 3, 0])
        )
        dictionary.edit("Hello", 11)
        self.assertEqual(
            dictionary.dictionary, (["Hello", "World", 0, "!", 0], [11, 2, 0, 3, 0])
        )
        dictionary.edit("World", 22)
        self.assertEqual(
            dictionary.dictionary, (["Hello", "World", 0, "!", 0], [11, 22, 0, 3, 0])
        )
        with self.assertRaises(ValueError):
            dictionary.edit("Goodbye", 1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
