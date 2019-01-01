"""
Basic Linked List operations:
1. Insertion
    1.1 Insertion at the end
    1.2 Insertion at the front
2. Removing
    1.1 Removing at the end
    1.2 Removing at the front
3. Searching
4. Sorting
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_node(h, d):
    new_node = Node(d)
    if h is None:
        h = new_node
        new_node.next = None
    else:
        new_node.next = h
        h = new_node
    return h


def traverse(h):
    while h is not None:
        print(h.data)
        h = h.next


def insert_at_end(h, d):
    new_node = Node(d)
    while h.next is not None:
        h = h.next
    h.next = new_node
    h.next.data = new_node.data


def remove_at_end(h, l):
    while l - 2:
        h = h.next
        l -= 1
    h.next = None


def size(h):
    len = 0
    while h is not None:
        h = h.next
        len += 1
    return len


def remove_at_front(h):
    h = h.next
    return h


def search(h, d):
    found = False
    while h is not None:
        if d == h.data:
            found = True
            break
        h = h.next
    if found:
        print("Element %d is present" % d)
    else:
        print("Element %d is not present" % d)
    return d


def sort(h, l):
    while h is not None:
        t = h
        while t is not None:
            if h.data > t.data:
                temp = h.data
                h.data = t.data
                t.data = temp
            t = t.next
        h = h.next


if __name__ == '__main__':
    head = None
    head = insert_node(head, 6)
    head = insert_node(head, 5)
    head = insert_node(head, 8)
    head = insert_node(head, 7)
    insert_at_end(head, 1)
    insert_at_end(head, 4)
    length = size(head)
    remove_at_end(head, length)
    head = remove_at_front(head)
    search(head, 81)
    sort(head, length)
    traverse(head)
