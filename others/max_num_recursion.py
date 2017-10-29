import math

def max_num(A, left, right):
	if left == right:
		return A[left]
	else:
		mid = int(math.floor((left + right)/2))
		lmax = max_num(A, left, mid)
		rmax = max_num(A, mid+1, right)
		if lmax > rmax:
			return lmax
		else:
			return rmax
print max_num([-2,3,4,-8,19,5,67, 33], 0, 7)
