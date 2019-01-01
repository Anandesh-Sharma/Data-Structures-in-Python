"""
Basic Array operations:
1. Insertion
    1.1 Insertion at the end
    1.2 Insertion at the front
    1.3 Insertion at the ith index
2. Removing
    1.1 Removing at the end
    1.2 Removing at the front
    1.3 Removing at the ith index
3. Searching
4. Sorting
"""

import random


def create_array(n):
    a = []
    for i in range(n):
        a.append(random.randint(0, 100))
    return a


def insert_at_end(a, x):
    a.append(x)
    print("After inserting element %d at end" % x)
    print(a)


def insert_at_front(a, x):
    a.append(0)
    s = a.__len__()
    for i in range(s - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = x
    print("After inserting element %d at front" % x)
    print(a)


def search(a, x):
    print("Searching element %d" % x)
    found = False
    for i in a:
        if x == i:
            found = True
            break
    if found:
        print("Element is present")
    else:
        print("Element is not present")


def insert_at_index(a, x, i):
    a.append(0)
    s = a.__len__()
    for j in range(s - 1, i - 1, -1):
        a[j] = a[j - 1]
    a[i] = x
    print("After inserting element %d at index %d" % (x, i))
    print(a)


def remove_at_end(a):
    return a[:-1]


def remove_at_front(a):
    return a[1:]


def remove_at_index(a, i):
    s = a.__len__()
    for j in range(i, s - 1):
        a[j] = a[j + 1]
    return a[:-1]


def sort(a):
    a.sort()
    # any sorting can be implemented


if __name__ == '__main__':
    arr = create_array(10)
    insert_at_end(arr, 5)
    insert_at_front(arr, 4)
    insert_at_index(arr, 8, 5)
    arr = remove_at_end(arr)
    print("After removing at end")
    print(arr)
    arr = remove_at_front(arr)
    print("After removing at front")
    print(arr)
    arr = remove_at_index(arr, 5)
    print("After removing at index")
    print(arr)
    sort(arr)
    print("After sorting the array")
    print(arr)
    search(arr, 8)
