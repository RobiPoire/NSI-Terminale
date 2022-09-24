"""
The abstract types - Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Functions to test the abstract linear data types of lists, stacks and queues implemented in Python
"""

__author__ = "RobiPoire"

from abstract_types import Lists, Stacks, Queues


def test_list_creation():
    """Test the creation of a list"""
    print("Test the creation of a list")
    list = Lists(5)
    assert list.size == 5
    assert list.list == [0, 0, 0, 0, 0, 0]
    print("Test passed")


def test_list_insert():
    """Test the insertion of an element in a list"""
    print("Test the insertion of an element in a list")
    list = Lists(5)
    list.insert("Hello", 1)
    assert list.list == [1, "Hello", 0, 0, 0, 0]
    list.insert("World", 2)
    assert list.list == [2, "Hello", "World", 0, 0, 0]
    list.insert("!", 3)
    assert list.list == [3, "Hello", "World", "!", 0, 0]
    print("Test passed")


def test_list_delete():
    """Test the deletion of an element in a list"""
    print("Test the deletion of an element in a list")
    list = Lists(5)
    list.insert("Hello", 1)
    list.insert("World", 2)
    list.insert("!", 3)
    list.delete(1)
    assert list.list == [2, "World", "!", 0, 0, 0]
    list.delete(2)
    assert list.list == [1, 'World', 0, 0, 0, 0]
    list.delete(1)
    assert list.list == [0, 0, 0, 0, 0, 0]
    print("Test passed")


def test_list_full():
    """Test the fullness of a list"""
    print("Test the fullness of a list")
    list = Lists(5)
    assert list.is_full() == False
    list.insert("Hello", 1)
    list.insert("World", 2)
    list.insert("!", 3)
    list.insert("Hello", 4)
    list.insert("World", 5)
    assert list.is_full() == True
    print("Test passed")


def test_list_empty():
    """Test the emptiness of a list"""
    print("Test the emptiness of a list")
    list = Lists(5)
    assert list.is_empty() == True
    list.insert("Hello", 1)
    assert list.is_empty() == False
    print("Test passed")


def test_list_search():
    """Test the search of an element in a list"""
    print("Test the search of an element in a list")
    list = Lists(5)
    list.insert("Hello", 1)
    list.insert("World", 2)
    list.insert("!", 3)
    assert list.search("Hello") == 1
    assert list.search("World") == 2
    assert list.search("!") == 3
    try:
        list.search("Test")
    except ValueError:
        print("Test passed")


def test_list_str():
    """Test the display of a list"""
    print("Test the display of a list")
    list = Lists(5)
    list.insert("Hello", 1)
    list.insert("World", 2)
    list.insert("!", 3)
    assert str(list) == "[3, 'Hello', 'World', '!', 0, 0]"
    print("Test passed")


def tests_list():
    """Test all the functions of a list"""
    test_list_creation()
    test_list_insert()
    test_list_delete()
    test_list_full()
    test_list_empty()
    test_list_search()
    test_list_str()


def test_stack_creation():
    """Test the creation of a stack"""
    print("Test the creation of a stack")
    stack = Stacks(5)
    assert stack.stack == [1, 0, 0, 0, 0, 0]
    print("Test passed")


def test_stack_add():
    """Test the addition of an element in a stack"""
    print("Test the addition of an element in a stack")
    stack = Stacks(5)
    stack.add("Hello")
    assert stack.stack == [2, "Hello", 0, 0, 0, 0]
    stack.add("World")
    assert stack.stack == [3, "Hello", "World", 0, 0, 0]
    stack.add("!")
    assert stack.stack == [4, "Hello", "World", "!", 0, 0]
    print("Test passed")


def test_stack_retrieve():
    """Test the retrieval of an element in a stack"""
    print("Test the retrieval of an element in a stack")
    stack = Stacks(5)
    stack.add("Hello")
    stack.add("World")
    stack.add("!")
    assert stack.retrieve() == "!"
    assert stack.stack == [3, "Hello", "World", "!", 0, 0]
    assert stack.retrieve() == "World"
    assert stack.stack == [2, "Hello", "World", "!", 0, 0]
    assert stack.retrieve() == "Hello"
    assert stack.stack == [1, "Hello", "World", "!", 0, 0]
    print("Test passed")


def test_stack_full():
    """Test the fullness of a stack"""
    print("Test the fullness of a stack")
    stack = Stacks(5)
    assert stack.is_full() == False
    stack.add("Hello")
    stack.add("World")
    stack.add("!")
    stack.add("Hello")
    stack.add("World")
    assert stack.is_full() == True
    print("Test passed")


def test_stack_empty():
    """Test the emptiness of a stack"""
    print("Test the emptiness of a stack")
    stack = Stacks(5)
    assert stack.is_empty() == True
    stack.add("Hello")
    assert stack.is_empty() == False
    print("Test passed")


def test_stack_str():
    """Test the display of a stack"""
    print("Test the display of a stack")
    stack = Stacks(5)
    stack.add("Hello")
    stack.add("World")
    stack.add("!")
    assert str(stack) == "[4, 'Hello', 'World', '!', 0, 0]"
    print("Test passed")


def tests_stack():
    """Test all the functions of a stack"""
    test_stack_creation()
    test_stack_add()
    test_stack_retrieve()
    test_stack_full()
    test_stack_empty()
    test_stack_str()


def test_queue_creation():
    """Test the creation of a queue"""
    print("Test the creation of a queue")
    queue = Queues(5)
    assert queue.size == 5
    assert queue.queue == [3, 3, 0, 0, 0, 0, 0, 0]
    print("Test passed")


def test_queue_put():
    """Test the addition of an element in a queue"""
    print("Test the addition of an element in a queue")
    queue = Queues(5)
    queue.put("Hello")
    assert queue.queue == [3, 4, 1, "Hello", 0, 0, 0, 0]
    queue.put("World")
    assert queue.queue == [3, 5, 2, "Hello", "World", 0, 0, 0]
    queue.put("!")
    assert queue.queue == [3, 6, 3, "Hello", "World", "!", 0, 0]
    print("Test passed")


def test_queue_get():
    """Test the retrieval of an element in a queue"""
    print("Test the retrieval of an element in a queue")
    queue = Queues(5)
    queue.put("Hello")
    queue.put("World")
    queue.put("!")
    assert queue.get() == "Hello"
    assert queue.queue == [4, 6, 2, 'Hello', 'World', '!', 0, 0]
    assert queue.get() == "World"
    assert queue.queue == [5, 6, 1, 'Hello', 'World', '!', 0, 0]
    assert queue.get() == "!"
    assert queue.queue == [6, 6, 0, 'Hello', 'World', '!', 0, 0]
    print("Test passed")


def test_queue_full():
    """Test the fullness of a queue"""
    print("Test the fullness of a queue")
    queue = Queues(5)
    assert queue.is_full() == False
    queue.put("Hello")
    queue.put("World")
    queue.put("!")
    queue.put("Hello")
    queue.put("World")
    assert queue.is_full() == True
    print("Test passed")


def test_queue_empty():
    """Test the emptiness of a queue"""
    print("Test the emptiness of a queue")
    queue = Queues(5)
    assert queue.is_empty() == True
    queue.put("Hello")
    assert queue.is_empty() == False
    print("Test passed")


def test_queue_str():
    """Test the display of a queue"""
    print("Test the display of a queue")
    queue = Queues(5)
    queue.put("Hello")
    queue.put("World")
    queue.put("!")
    assert str(queue) == "[3, 6, 3, 'Hello', 'World', '!', 0, 0]"
    print("Test passed")


def tests_queue():
    """Test all the functions of a queue"""
    test_queue_creation()
    test_queue_put()
    test_queue_get()
    test_queue_full()
    test_queue_empty()
    test_queue_str()


def all_tests():
    """Test all the functions"""
    tests_list()
    tests_stack()
    tests_queue()


all_tests()
