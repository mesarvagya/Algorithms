import math
from copy import deepcopy

def MergeSort(A, p, r):
    if p < r:
        q = int(math.floor((p + r) / 2))
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)

def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    ## Create two temporary arrays of len n1 and n2
    L = [0] * n1
    R = [0] * n2

    ### Copy contents into L and R
    for i in xrange(n1):
        L[i] = A[p + i]
    for j in xrange(n2):
        R[j] = A[q + j + 1]

    ## Create pointers i, j, k to keep track of merging correctly.
    i = 0; j = 0; k = p;
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    ### Check if some array is empty. If so copy it to the end
    while i < n1:
        A[k] = L[i]
        k += 1
        i += 1

    while j < n2:
        A[k] = R[j]
        k += 1
        j += 1

A = [2, 8, 7, 1 , 3, 6, 5 , 4, 13, 9, 12, 8, 14]
B = deepcopy(A)

MergeSort(A, 0, len(A) - 1)
assert(A == sorted(B))

print A


