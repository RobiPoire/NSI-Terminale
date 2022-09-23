"""
The abstract types
~~~~~~~~~~~~~~~~~~~
Functions of abstract linear data types of lists, stacks and queues implemented in Python
"""

__author__ = "HabibLebsir, devnatiofrance and RobiPoire"


class Lists:
    """The abstract type of lists"""

    def __init__(self, size: int) -> None:
        """Create a list with the chosen size

        Args:
            size (int): The size of the list

        Raises:
            ValueError: If the size is less than 1
        """
        if size < 1:
            raise ValueError("Size must be greater than 0")
        self.size = size # The size of the list
        self.list = [0] * (self.size + 1) # The list wi

    def __str__(self) -> str:
        """Display the list

        Returns:
            str: The list
        """
        return f"{self.list}"

    def insert(self, element: object, index: int) -> None:
        """Insert an element at the chosen index

        Args:
            element (object): The element to insert
            index (int): The index to insert the element

        Raises:
            IndexError: If the index is 0
            IndexError: If the list is full
        """
        if index == 0:
            raise IndexError(
                "Index 0 is reserved for the length of the list")
        if self.is_full():
            raise IndexError(
                f"List is full, can't insert {element}, max size is {self.size}")
        self.list[0] += 1
        self.list[index] = element

    def delete(self, index: int) -> None:
        """Delete an element at the chosen index

        Args:
            index (int): The index to delete the element

        Raises:
            IndexError: If the index is 0
            IndexError: If the list is empty
        """
        if index == 0:
            raise IndexError(
                "Index 0 is reserved for the length of the list")
        if self.is_empty():
            raise IndexError("List is empty")
        self.list[0] = self.list[0] - 1
        for i in range(index + 1, self.size + 1):
            self.list[i-1] = self.list[i]

    def search(self, element: object) -> int:
        """Search an element in the list

        Args:
            element (object): The element to search

        Raises:
            ValueError: If the element is not in the list

        Returns:
            int: The index of the element
        """
        for position in range(1, self.length()+1):
            if self.list[position] == element:
                return position
        raise ValueError(f"{element} is not in the list")

    def read(self, index: int) -> object:
        """Read an element at the chosen index

        Args:
            index (int): The index to read the element

        Raises:
            IndexError: If the index is 0

        Returns:
            object: The element at the chosen index
        """
        if index == 0:
            raise IndexError(
                "Index 0 is reserved for the length of the list")
        return self.list[index]

    def change(self, index: int, element: object) -> None:
        """Change an element at the chosen index

        Args:
            index (int): The index to change the element
            element (object): The element to change

        Raises:
            IndexError: If the index is 0
        """
        if index == 0:
            raise IndexError(
                "Index 0 is reserved for the length of the list")
        self.list[index] = element

    def length(self) -> int:
        """Length of the list

        Returns:
            int: The length of the list
        """
        return self.list[0]

    def is_empty(self) -> bool:
        """Is the list empty

        Returns:
            bool: True if the list is empty, False otherwise
        """
        return self.length() == 0

    def is_full(self) -> bool:
        """Is the list full

        Returns:
            bool: True if the list is full, False otherwise
        """
        return self.list[0] == self.size


class Stacks:
    """The abstract type of stacks"""

    def __init__(self, size: int):
        """Create a stack with the chosen size

        Args:
            size (int): The size of the stack

        Raises:
            ValueError: If the size is less than 1
        """
        if size < 1:
            raise ValueError("Size must be greater than 0")
        self.size = size
        self.stack = [1]+[0]*(self.size)

    def __str__(self) -> str:
        """Display the stack

        Returns:
            str: The stack
        """
        return f"{self.stack}"

    def add(self, element: object) -> None:
        """Add an element to the stack

        Args:
            element (object): The element to add

        Raises:
            IndexError: If the stack is full
        """
        if self.is_full():
            raise IndexError(
                f"Stack is full, can't add {element}, max size is {self.size}")
        self.stack[self.stack[0]] = element
        self.stack[0] = self.stack[0] + 1

    def retrieve(self) -> int:
        """Retrieve the last element of the stack

        Raises:
            IndexError: If the stack is empty

        Returns:
            int: The last element of the stack
        """
        if self.is_empty():
            raise IndexError("Stack is empty, can't retrieve")
        element = self.stack[self.stack[0] - 1]
        self.stack[self.stack[0] - 1] = 0
        self.stack[0] = self.stack[0] - 1
        return (element)

    def is_empty(self) -> bool:
        """Is the stack empty

        Returns:
            bool: True if the stack is empty, False otherwise
        """
        return self.stack[0] == 1

    def is_full(self) -> bool:
        """Is the stack full

        Returns:
            bool: True if the stack is full, False otherwise
        """
        return self.stack[0] == self.size + 1


class Queues:
    """The abstract type of queues"""

    def __init__(self, size: int) -> None:
        """Create a queue with the chosen size

        Args:
            size (int): The size of the queue
        """
        self.size = size
        self.queue = [3, 3, 0]+[0]*self.size

    def __str__(self) -> str:
        """Display the queue

        Returns:
            str: The queue
        """
        return f"{self.queue}"

    def put(self, element: object) -> None:
        """Put an element in the queue

        Args:
            element (object): The element to put

        Raises:
            IndexError: If the queue is full
        """
        if self.is_full():
            raise IndexError(
                f"Queue is full, can't add {element}, max size is {self.size}")
        self.queue[self.queue[1]] = element
        self.queue[2] += 1
        self.queue[1] = 3 if self.queue[1] == self.size+2 else self.queue[1]+1

    def get(self) -> object:
        """Get an element from the queue

        Raises:
            IndexError: If the queue is empty

        Returns:
            object: The element from the queue
        """
        if self.is_empty():
            raise IndexError(
                "Queue is empty, can't get an element")
        element = self.queue[self.queue[0]]
        self.queue[0] = 3 if self.queue[0] == self.size+2 else self.queue[0]+1
        self.queue[2] -= 1
        return element

    def is_empty(self) -> bool:
        """Is the queue empty

        Returns:
            bool: True if the queue is empty, False otherwise
        """
        return self.queue[2] == 0

    def is_full(self) -> bool:
        """Is the queue full

        Returns:
            bool: True if the queue is full, False otherwise
        """
        return self.queue[2] == self.size
