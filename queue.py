#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if self.list.length() != 0:
            return False
        else:
            return True

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        queue_length = self.list.length()
        return queue_length

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? [the logic follows a straight line
        without needing to loop]"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.list.length() != 0:
            # index = self.length() - 1
            front = self.list.get_at_index(0)
            return front
        else:
            return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) – Why? [pop() calls peek() that calls length() from
        LinkedList, which iterates using a while loop]"""
        # TODO: Remove and return front item, if any
        # find top_item
        if self.list.length() != 0:
            front = self.list.get_at_index(0)
            # delete top_item
            self.list.delete(front)
            return front
        else:
            raise ValueError('Queue is Empty')

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if self.front() is None:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        qa_length = len(self.list)
        return qa_length

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? [adding item to end of list requires no
        complex data manipulation nor looping]"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if len(self.list) == 0:
            return None
        else:
            front_item = self.list[0]
            return front_item

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) – Why? [all items in the array must shift
        left when an item is dequeued because the front of the queue is
        at index zero]"""
        # TODO: Remove and return front item, if any
        front = self.front()
        if front is None:
            raise ValueError('List is Empty')
        else:
            print('Dequeued item: ', front)
            self.list.pop(0)
            return front


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
