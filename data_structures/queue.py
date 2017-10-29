class Queue(object):
    def __init__(self, size = 100):
        self.size = size
        self.arr = [None for _ in xrange(size)]
        self.front = 0
        self.rear = -1
        self.nElems = 0

    def enqueue(self, item):
        # If rear reaches the max size, wrap it around.
        if self.rear == self.size - 1:
            self.rear = -1
        self.rear += 1
        self.arr[self.rear] = item
        self.nElems += 1

    def dequeue(self):
        temp = self.arr[self.front]
        self.front += 1

        # If front reaches the size, wrap it around.
        if self.front == self.size:
            self.front = 0
        self.nElems -= 1
        return temp

    def empty(self):
        return self.nElems == 0

    def full(self):
        return self.nElems == self.size

    def peekfront(self):
        return self.arr[self.front]

    def size(self):
        return self.nElems

    def __str__(self):
        q = " ".join(map(str, self.arr))
        return "Queue size %d actual %s" % (self.size, q )

if __name__ == "__main__":
    q = Queue(size=5)
    print q.empty()
    for _ in xrange(5):
        q.enqueue(_)
    print q.full()
    print q
    while not q.empty():
        print q.dequeue(),