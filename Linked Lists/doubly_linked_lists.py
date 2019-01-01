class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def add_node(h, d):
    new_node = Node(d)
    if h is None:
        h = new_node
    else:
        h.prev = new_node
        new_node.next = h
        h = new_node
    return h


def traverse(h):
    while h is not None:
        print(h.data)
        h = h.next


def traverse_back(h):
    while h.next is not None:
        h = h.next

    while h is not None:
        print(h.data)
        h = h.prev


if __name__ == '__main__':
    head = None
    head = add_node(head, 10)
    head = add_node(head, 20)
    head = add_node(head, 30)

    traverse(head)
    traverse_back(head)
