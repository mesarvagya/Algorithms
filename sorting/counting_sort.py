A = [3,1,4,5,2,3,1,6,4,0,2,0,4,1,0,1,2]
def counting_sort(A, B, k):
    C = [0 for i in range(k+1)]
    for item in A:
        C[item] = C[item] + 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    print "C = ", C
    for j in range(len(A) - 1, -1, -1):
        index_b = C[A[j]] - 1
        B[index_b] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B

B = [0 for i in range(len(A))]

data = counting_sort(A, B, k=6)
data2 = sorted(A)

assert(data == data2)

print B