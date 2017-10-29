def recMax(A, index):
    if(len(A) == index):
        return A[index-1]
    submax = recMax(A, index+1)
    remmax = 0
    for i in range(index, len(A), 1):
        remmax += A[i]
        if remmax > submax:
            submax = remmax
    return submax

print recMax([-2, -3, 4, -1, -2, 1, 5, -3], 0)
