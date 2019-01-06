class Stack:
    def __init__(self):
        self.A = []

    def pop(self):
        len = self.A.__len__()
        e = self.A[len - 1]
        self.A = self.A[:-1]
        return e

    def push(self, d):
        self.A.append(d)

    def print(self):
        print(self.A)


if __name__ == '__main__':
    myStack = Stack()
    myStack.push(5)
    myStack.push(6)
    myStack.push(7)
    myStack.push(8)
    myStack.push(9)
    print(myStack.pop())
    myStack.print()

