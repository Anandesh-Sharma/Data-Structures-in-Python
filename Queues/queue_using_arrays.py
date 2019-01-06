class Queue:
    def __init__(self):
        self.A = []

    def push(self, d):
        self.A.append(d)

    def pop(self):
        d = self.A[0]
        self.A = self.A[1:]
        return d

    def print(self):
        print(self.A)


if __name__ == '__main__':
    myQueue = Queue()
    myQueue.push(10)
    myQueue.push(20)
    myQueue.push(30)
    myQueue.push(40)
    myQueue.push(50)

    print(myQueue.pop())
    print(myQueue.pop())
    myQueue.push(60)

    myQueue.print()
