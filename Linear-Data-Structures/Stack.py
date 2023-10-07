# Data Structure: Stack Implementation (Using Doubly-Linked List)

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


class Stack:
    """
    A class to represent a Stack.

    ...
    Attributes
    ----------
    head: Node
        hold the last element pushed onto the stack.
    tail: Node
        hold the first element pushed onto the stack.
    traverse: Node
        hold the current element traversed.

    Methods
    -------
    push(value: Node)
        Adds an element to the start of the Stack. (O(1))
    pop()
        Removes an element from the start of the Stack. (O(1))
    peek(last: Boolean)
        Look at the top / last element of the Stack. (O(1))
    traversal(back: Boolean)
        Traverse the stack, like a browsing session. (O(1))
    print_links()
        :returns a string showing a Node's value, it's previous value (if any), it's next value (if any).
    __print_helper_links(head: Node)
        A helper function for print_links()
    """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.traverse = self.head

    def push(self, value):
        node = Node(value)

        # Case 1: First Element in Stack
        if not self.head:
            self.head = node
            self.tail = node

        # Case 2: More than 1 Element in Stack
        elif self.head:
            self.head.previous = node
            node.next, self.head = self.head, node
            self.traverse = node

    def pop(self):

        # Case 1: No Elements
        if not self.head:
            raise IndexError("Stack is empty.")

        # Case 2: Only 1 Element in the Stack
        elif not self.head.next:
            self.head, self.tail, self.traverse = None, None, None

        # Case 3: More than 1 Element in Stack
        else:
            self.head, self.head.previous = self.head.next, None
            self.traverse = self.head

    def peek(self, last=False):

        # If Stack has at-least 1 element.
        if self.head:

            # Peek: Oldest Element
            if last:
                return self.tail.value

            # Peek: Latest Element
            elif not last:
                return self.head.value

        # If Stack is Empty.
        raise IndexError("Stack is empty.")

    def traversal(self, back=True):

        # If Stack has at-least 1 element.
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

        # If Stack is Empty.
        raise IndexError("Stack is empty.")

    def print_links(self):
        if not self.head:
            raise IndexError("Stack is empty.")

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

    # Initialize a Stack Object.
    stack = Stack()

    # Push Elements onto the Stack.
    stack.push(1)  # 1
    stack.push(2)  # 2 <--> 1
    stack.push(3)  # 3 <--> 2 <--> 1

    # Pop Elements from the Stack.
    stack.pop()  # 2 <--> 1

    # Traverse our Stack.
    print(stack.traversal(back=True))   # 1
    print(stack.traversal(back=False))  # 2

    # Print our Stack (with Links)
    print(stack.print_links())
