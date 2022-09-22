from abstract_types import Lists, Stacks, Queues

# Create a list
list = Lists(5)

# Insert elements
list.insert(1, 1)
list.insert(2, 2)
list.insert(3, 3)
list.insert(4, 4)
print(list)

# Delete an element
list.delete(1)
print(list)

# Search an element
print(list.search(3))

# Read an element
print(list.read(2))

# Change an element
list.change(2, 5)
print(list)

# length of the list
print(list.length())

print("-----------------------------")

# Create a stack
stack = Stacks(5)

# add elements
stack.add(1)
stack.add(2)
stack.add(3)
stack.add(4)
print(stack)

# retrieve an element
print(stack.retrieve())
print(stack.retrieve())
print(stack.retrieve())
print(stack)

print("-----------------------------")

# Create a queue
queue = Queues(5)

# put elements
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
print(queue)

# get an element
print(queue.get())
print(queue)