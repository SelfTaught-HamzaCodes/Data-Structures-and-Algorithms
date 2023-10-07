# Data Structure: Queue Implementation (Using Doubly-Linked List)

class Node:

    def __init__(self, value, previous_=None, next_=None):
        """
        Initializes a Node, with a value, previous reference and next reference.

        :param value (any): Any value.
        :param previous_ (Node): Reference to the previous Node.
        :param next_ (Node): Reference to the next Node.
        """
        self.value = value
        self.previous = previous_
        self.next = next_


class Queue:
    """
    A class to represent a Queue.

    ...
    Attributes
    ----------
    head: Node
        hold the first element in a queue.
    tail: Node
        hold the last element in a queue.
    traverse: Node
        hold the current element traversed.

    Methods
    -------
    enqueue(value: Node)
        Adds an element to the end of the Queue. (O(1))
    deque()
        Removes an element from the start of the Queue. (O(1))
    peek(last: Boolean)
        Look at the first / last element of the Queue. (O(1))
    traversal(back: Boolean)
        Traverse the queue, like a browsing session. (O(1))
    print_links()
        :returns a string showing a Node's value, it's previous value (if any), it's next value (if any).
    __print_helper_links(head: Node)
        A helper function for print_links()
    """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.traverse = self.head

    def enqueue(self, value):
        node = Node(value)

        # Case 1: First Element in Queue.
        if not self.head:
            self.head = node
            self.tail = node

        # Case 2: More than 1 Element in Queue.
        elif self.head:
            self.tail.previous = node
            node.previous = self.tail
            self.tail.next, self.tail = node, node

    def deque(self):

        # Case 1: No Elements
        if not self.head:
            raise IndexError("Queue is empty.")

        # Case 2: Only 1 Element in the Queue.
        elif not self.head.next:
            self.head, self.tail, self.traverse = None, None, None

        # Case 3: More than 1 Element in Queue.
        else:
            self.head, self.head.previous = self.head.next, None
            self.traverse = self.head

    def peek(self, last=False):

        # If Queue has at-least 1 element.
        if self.head:

            # Peek: Oldest Element
            if last:
                return self.tail.value

            # Peek: Latest Element
            elif not last:
                return self.head.value

        # If Queue is Empty.
        raise IndexError("Queue is empty.")

    def traversal(self, back=True):

        # If Queue has at-least 1 element.
        if self.head:

            # To traverse backwards / downwards (next)
            if back:
                if self.traverse.next:
                    self.traverse = self.traverse.next
                    return self.traverse.value

                return "No backwards traversals possible."

            # To traverse forwards / upwards (previous)
            if not back:
                if self.traverse.previous:
                    self.traverse = self.traverse.previous
                    return self.traverse.value

                return "No forward traversals possible."

        # If Queue is Empty.
        raise IndexError("Queue is empty.")

    def print_links(self):
        if not self.head:
            raise IndexError("Queue is empty.")

        else:
            return self.__print_helper_links(self.head)

    def __print_helper_links(self, head):

        # Base Case:
        if not head.next:
            return F"Value:({str(head.value)})" \
                   + F" Previous: {head.previous.value if head.previous else head.previous} |" \
                     F" Next: {head.next.value if head.next else head.next}"

        else:
            return F"Value:({str(head.value)})" + \
                   F" Previous: {head.previous.value if head.previous else head.previous} |" \
                   F" Next: {head.next.value} " + \
                   " <-> " + self.__print_helper_links(head.next)


if __name__ == "__main__":

    # Initialize a Queue Object.
    queue = Queue()

    # Push Elements onto the Queue.
    queue.enqueue(1)  # 1
    queue.enqueue(2)  # 1 <--> 2
    queue.enqueue(3)  # 1 <--> 2 <--> 3

    # Pop Elements from the Queue.
    queue.deque()  # 2 <--> 3

    # Traverse our Queue.
    print(queue.traversal(back=True))   # 3
    print(queue.traversal(back=False))  # 2

    # Print our Queue (with Links)
    print(queue.print_links())
