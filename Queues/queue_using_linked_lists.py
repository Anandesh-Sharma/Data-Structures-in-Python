class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def push(self, d, h):
        new_node = Node(d)
        if h is None:
            h = new_node
        else:
            new_node.next = h
            h = new_node
        return h

    def pop(self, h):
        while h.next.next is not None:
            h = h.next
        d = h.next.data
        h.next = None
        return d

    def print(self, h):
        while h is not None:
            print(h.data)
            h = h.next


if __name__ == '__main__':
    head = None
    myQueue = Queue()
    head = myQueue.push(10, head)
    head = myQueue.push(20, head)
    head = myQueue.push(30, head)
    head = myQueue.push(40, head)
    myQueue.pop(head)
    myQueue.pop(head)

    # print(myQueue.pop(head), "is popped out")
    # print(myQueue.pop(head), "is popped out")
    myQueue.print(head)
