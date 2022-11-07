"""
The abstract types
~~~~~~~~~~~~~~~~~~~
Functions of abstract linear data types of lists, stacks, queues and dictionaries implemented in Python
"""

__author__ = "HabibLebsir, devnatiofrance and RobiPoire"


from typing import Any


class Lists:
    """The abstract type of lists"""

    def __init__(self, size: int) -> None:
        """Constructor of the class Lists

        Args:
            size (int): The size of the list

        Raises:
            ValueError: If the size is less than 1
        """
        if size < 1:
            raise ValueError("Size must be greater than 0")
        self.size = size  # The size of the list
        self.list = [0] * (self.size + 1)  # The list wi

    def __str__(self) -> str:
        """Summary of the list

        Returns:
            str: The summary of the list
        """
        output = f"Length/Size: {self.list[0]}/{self.size}\nList: {self.list[1:]}"
        return output

    def insert(self, element: Any, index: int) -> None:
        """Insert an element at the chosen index

        Args:
            element (Any): The element to insert
            index (int): The index to insert the element

        Raises:
            IndexError: If the index is 0
            IndexError: If the list is full
        """
        if index == 0:
            raise IndexError("Index 0 is reserved for the length of the list")
        if self.is_full():
            raise IndexError(
                f"List is full, can't insert {element}, max size is {self.size}"
            )
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
            raise IndexError("Index 0 is reserved for the length of the list")
        if self.is_empty():
            raise IndexError("List is empty")
        self.list[0] = self.list[0] - 1  # Decrease the length of the list
        for i in range(index + 1, self.size + 1):
            self.list[i - 1] = self.list[i]  # Shift the elements to the left

    def search(self, element: Any) -> int | None:
        """Search an element in the list

        Args:
            element (Any): The element to search

        Returns:
            int|None: The index of the element if found, None otherwise
        """
        for position in range(1, self.list[0] + 1):
            if (
                self.list[position] == element
            ):  # If the element is found, return the index
                return position
        return None

    def read(self, index: int) -> Any:
        """Read an element at the chosen index

        Args:
            index (int): The index to read the element

        Raises:
            IndexError: If the index is 0

        Returns:
            Any: The element at the chosen index
        """
        if index == 0:
            raise IndexError("Index 0 is reserved for the length of the list")
        return self.list[index]

    def change(self, index: int, element: Any) -> None:
        """Change an element at the chosen index

        Args:
            index (int): The index to change the element
            element (Any): The element to change

        Raises:
            IndexError: If the index is 0
        """
        if index == 0:
            raise IndexError("Index 0 is reserved for the length of the list")
        self.list[index] = element  # Change the element at the chosen index

    def is_empty(self) -> bool:
        """Is the list empty

        Returns:
            bool: True if the list is empty, False otherwise
        """
        return self.list[0] == 0

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
        self.size = size  # The size of the stack
        # The stack with the first element as the length of the stack
        self.stack = [1] + [0] * (self.size)

    def __str__(self) -> str:
        """Display the stack

        Returns:
            str: The stack
        """
        output = f"Lenght/Size: {self.stack[0]-1}/{self.size}\nLast element index: {self.stack[1]}\nStack: {self.stack[2:]}"
        return output

    def push(self, element: Any) -> None:
        """Add an element to the stack

        Args:
            element (Any): The element to add

        Raises:
            IndexError: If the stack is full
        """
        if self.is_full():
            raise IndexError(
                f"Stack is full, can't add {element}, max size is {self.size}"
            )
        self.stack[self.stack[0]] = element  # Add the element to the stack
        self.stack[0] += 1

    def pop(self) -> int:
        """Retrieve the last element of the stack

        Raises:
            IndexError: If the stack is empty

        Returns:
            int: The last element of the stack
        """
        if self.is_empty():
            raise IndexError("Stack is empty, can't retrieve")
        # Recover the last element of the stack
        element = self.stack[self.stack[0] - 1]
        self.stack[0] -= 1  # Decrease the length of the stack
        return element  # Return the last element of the stack

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
        self.size = size  # The size of the queue
        # The queue with the first element as the length of the queue, the second element as the
        # first element of the queue and the third element as the last element of the queue
        self.queue = [3, 3, 0] + [0] * self.size

    def __str__(self) -> str:
        """Display the queue

        Returns:
            str: The queue
        """
        output = f"Firt element index: {self.queue[0]}\n \
                    Last element index: {self.queue[1]}\n \
                    Length/Size: {self.queue[2]}/{self.size}\n \
                    Queue: {self.queue[3:]}"
        return output

    def enqueue(self, element: Any) -> None:
        """Add an element to the queue

        Args:
            element (Any): The element to put

        Raises:
            IndexError: If the queue is full
        """
        if self.is_full():
            raise IndexError(
                f"Queue is full, can't add {element}, max size is {self.size}"
            )
        self.queue[self.queue[1]] = element  # Put the element in the queue
        self.queue[2] += 1  # Increase the last element of the queue
        # Increase the first element of the queue or reset it to 3 if it's the last index of the queue
        self.queue[1] = 3 if self.queue[1] == self.size + 2 else self.queue[1] + 1

    def dequeue(self) -> Any:
        """Retrieve the first element of the queue

        Raises:
            IndexError: If the queue is empty

        Returns:
            Any: The element from the queue
        """
        if self.is_empty():
            raise IndexError("Queue is empty, can't get an element")
        element = self.queue[self.queue[0]]  # Get the element from the queue
        # Increase the first element of the queue or reset it to 3 if it's the last index of the queue
        self.queue[0] = 3 if self.queue[0] == self.size + 2 else self.queue[0] + 1
        self.queue[2] -= 1  # Decrease the last element of the queue
        return element  # Return the element from the queue

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


class Dictionaries:
    """The abstract type of dictionaries"""

    def __init__(self, size: int) -> None:
        """Create a dictionary with the chosen size

        Args:
            size (int): The size of the dictionary
        """
        self.size = size
        self.dictionary = ([0] * self.size, [0] * self.size)

    def __str__(self) -> str:
        """Display the summary of the dictionary

        Returns:
            str: The summary of the dictionary
        """
        output = f"Size:{self.size}\nKeys: {self.dictionary[0]}\nValues: {self.dictionary[1]}"
        return output

    def __hash(self, key: Any) -> int:
        """Hash the key to get the index of the value

        Args:
            key (Any): The key to hash

        Returns:
            int: The index of the value
        """
        hash_sum = 0
        for i in key:
            hash_sum += ord(i)
        return hash_sum % self.size

    def insert(self, key: Any, value: Any) -> None:
        """Insert a key and a value in the dictionary

        Args:
            key (Any): The key to insert
            value (Any): The value to insert

        Raises:
            IndexError: If the dictionary is full
        """
        keys, values = self.dictionary
        if self.is_full():
            raise IndexError(
                f"Dictionary is full, can't add {key}, max size is {self.size}"
            )
        if keys[self.__hash(key)] == 0:
            keys[self.__hash(key)] = key
            values[self.__hash(key)] = value
        else:
            for i in range(self.size):
                if keys[i] == 0:
                    keys[i] = key
                    values[i] = value
                    break

    def delete(self, key: Any) -> None:
        """Delete a key and a value from the dictionary

        Args:
            key (Any): The key to delete

        Raises:
            IndexError: If the dictionary is empty
            IndexError: If the key doesn't exist
        """
        keys, values = self.dictionary
        if self.is_empty():
            raise IndexError(f"Dictionary is empty, can't delete {key}")
        if keys[self.__hash(key)] == key:
            keys[self.__hash(key)] = 0
            values[self.__hash(key)] = 0
        else:
            for i in range(self.size):
                if keys[i] == key:
                    keys[i] = 0
                    values[i] = 0
                    return None
            raise IndexError(f"Dictionary doesn't contain {key}")

    def read(self, key: Any) -> Any:
        """Read a value from the dictionary

        Args:
            key (Any): The key to read

        Returns:
            Any: The value from the dictionary
        """
        keys, values = self.dictionary
        if keys[self.__hash(key)] == key:
            return values[self.__hash(key)]
        else:
            for i in range(self.size):
                if keys[i] == key:
                    return values[i]

    def research(self, value: Any) -> Any | None:
        """Research a key from the dictionary

        Args:
            value (Any): The value to research

        Returns:
            Any|None: The key from the dictionary or None if the value doesn't exist
        """
        keys, values = self.dictionary
        for i in range(self.size):
            if values[i] == value:
                return keys[i]
        return None  # If the value is not in the dictionary

    def edit(self, key: Any, value: Any) -> None:
        """Edit a value in the dictionary

        Args:
            key (Any): The key to edit
            value (Any): The new value

        Raises:
            IndexError: If the key doesn't exist
        """
        keys, values = self.dictionary
        if keys[self.__hash(key)] == key:
            values[self.__hash(key)] = value
        else:
            for i in range(self.size):
                if keys[i] == key:
                    values[i] = value
                    return None
            raise ValueError(f"Dictionary doesn't contain {key}")

    def is_empty(self) -> bool:
        """Is the dictionary empty

        Returns:
            bool: True if the dictionary is empty, False otherwise
        """
        keys = self.dictionary[0]
        for key in keys:
            if key != 0:
                return False
        return True

    def is_full(self) -> bool:
        """Is the dictionary full

        Returns:
            bool: True if the dictionary is full, False otherwise
        """
        keys = self.dictionary[0]
        for key in keys:
            if key == 0:
                return False
        return True
