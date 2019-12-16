
class MyQueue:
    def __init__(self, data=None):
        # Initialize this queue, and store data if it exists
        if data:
            self.head = Node(data)
            self.size = 1
        else:
            self.size= 0
            self.head = None

    def enqueue(self, data):
        # Add data to the end of the queue
        if not self.head:
            self.head = Node(data)
            return

        current_node = self.head

        while current_node:
            if current_node.next:
                current_node = current_node.next
            else:
                break

        current_node.next = Node(data)
        self.size += 1


    def dequeue(self):
        if not self.head:
            return None

        tmp = self.head
        self.head = self.head.next
        self.size -= 1
        return tmp.data


    def __len__(self):
        # Return the number of elements in the stack
        return self.size + 1
#
class MyStack:
    def __init__(self, data=None):
        # Initialize this stack, and store data if it exists
        if data:
            self.head = Node(data)
            self.size = 1
        else:
            self.size= 0
            self.head = None

    def push(self, data):
        # Add data to the beginning of the stack
        tmp = self.head
        self.head = Node(data)
        self.head.next = tmp
        self.size += 1

    def pop(self):
        # Return the data in the element at the beginning of the stack, or None if the stack is empty
        tmp = self.head
        self.head = tmp.next
        self.size += 1
        return tmp.data

    def __len__(self):
        # Return the number of elements in the stack
        return self.size


class Node:
    def __init__(self, data, next=None):
        # Initialize this node, insert data, and set the next node if any
        self.data = data
        if next:
            self.next = Node(next)
        else:
            self.next = None







