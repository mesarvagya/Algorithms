import heapq

class Node(object):
    def __init__(self, string, node, index, length):
        self.string = string
        self.node = node
        self.index = index
        self.length = length

    def __cmp__(self, other):
        return cmp(self.string, other.string)

    def __str__(self):
        return "string %s node %d index %d length %d" % (self.string, self.node, self.index, self.length)

a = ['this', 'array', 'is', 'to', 'be', 'sorted' , 'in', 'nlogk', 'time']
a = [sorted(x) for x in a]

heap = []
for i in xrange(len(a)):
    # Insert the front of each sorted array into the heap.
    heapq.heappush(heap, Node(a[i][0], i, 0, len(a[i])))

strr = []
while heap:
    h = heapq.heappop(heap)
    strr.append(h.string)
    ## Pop the minimum from heap and insert the other element from the corresponding array 
    ## of the popped element.
    if h.index + 1 < h.length:
        node = Node(a[h.node][h.index+1], h.node ,h.index+1, h.length)
        heapq.heappush(heap, node)

# assert that the length of characters in original string equals to that of when sorted.        
assert(len(strr) == reduce(lambda x,y : x+y, map(lambda x: len(x), a) ))
print ''.join(strr)
