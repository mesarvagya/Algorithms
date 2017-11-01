# -*- coding: utf-8 -*-

class ArrayStack(object):
    def __init__(self, len):
        self.len = len
        self.arr = [0 for _ in xrange(len)]
        self.nElems = 0

    # Constant time operations. θ(1)
    def get(self, i):
        if i < 0 or i > self.len - 1:
            raise IndexError("Invalid index used")
        return self.arr[i]

    # Constant time operations. θ(1)
    def set(self,i,x):
        if i < 0 or i > self.len - 1:
            raise IndexError("Invalid index used")
        temp = self.arr[i]
        self.arr[i] = x
        return temp

    # Add the element on the array stack
    def add(self, i, x):
        # If the elements being inserted at index i is < 0 or > current Elements, raise error.
        if i < 0 or i > self.nElems: return IndexError("Invalid index used")
        # is array full? resize it.
        elif self.nElems + 1 > len(self.arr): self.resize()
        # if everything is okay, insert the data at correct position and move others.
        for i in xrange(self.nElems, i, -1):
            self.arr[i+1] = self.arr[i]
        self.arr[i] = x
        self.nElems += 1

    def resize(self):
        # Create temp array of 2*n size
        new_arr = [0 for _ in xrange(2 * self.nElems)]
        # copy elements of original to temp.
        for i in xrange(self.nElems):
            new_arr[i] = self.arr[i]
        # point original to the newer one.
        self.arr = new_arr

    def remove(self, i):
        if i < 0 or i > self.nElems: return IndexError("Invalid index used")
        temp = self.arr[i]
        # shift down the numbers.
        for j in xrange(i, self.nElems):
            self.arr[j] = self.arr[j+1]
        self.nElems -= 1
        # if the array size is large, reduce it.
        if len(self.arr) > 3 * self.nElems: self.resize()
        return temp

    def __str__(self):
        return "[ " + " ".join(map(str,self.arr)) + " ]"

if __name__ == "__main__":
    arr = ArrayStack(5)
    arr.add(0, 5)
    arr.add(1, 4)
    arr.add(2, 3)
    arr.add(3, 2)
    arr.add(4, 1)
    # Since the original size was 5, we need to resize it here.
    arr.add(5, 6)
    arr.remove(0);arr.remove(0);arr.remove(0);arr.remove(0)
    print arr