class Stack(object):
    def __init__(self, size=100):
        self.data = [None for _ in xrange(size)]
        self.top = -1
        self.size = size

    def push(self, item):
        if not self.full():
            self.top += 1
            self.data[self.top] = item
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.empty():
            item = self.data[self.top]
            self.top -= 1
            return item
        else:
            raise ValueError("Stack is empty")
    
    def empty(self):
        return self.top == -1

    def full(self):
        return self.top == self.size - 1

    def __str__(self):
        stack = " ".join(map(str,self.data))

        return "Stack size %d filled %d actual %s" % (self.size, self.top + 1, stack)

if __name__ == "__main__":
    s = Stack(size=5)
    for _ in xrange(5):
        s.push(_)

    while not s.empty():
        print s.pop(),

