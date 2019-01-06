class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def push(self, d, h):
        new_node = Node(d)
        if h is None:
            h = new_node
        else:
            new_node.next = h
            h = new_node
        return h

    def pop(self, h):
        # e = h.data
        h = h.next
        return h

    def print(self, h):
        while h is not None:
            print(h.data)
            h = h.next


if __name__ == '__main__':
    head = None
    myStack = Stack()
    head = myStack.push(19, head)
    head = myStack.push(20, head)
    head = myStack.push(21, head)
    head = myStack.push(22, head)
    head = myStack.pop(head)
    head = myStack.pop(head)
    head = myStack.push(34, head)
    print(myStack.print(head))
