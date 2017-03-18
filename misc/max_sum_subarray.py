
def max_sum_subarray(A, p, q):
	if p == q : 
		return A[p]
	else:
		mid = (p + q) / 2
		print "mid ", mid
		lmax = max_sum_subarray(A, p, mid)
		rmax = max_sum_subarray(A, mid + 1, q)

		# Find the sum of subarray if it crosses the midpoint
		l = 0; llocalmax = A[mid];
		for i in range(mid, p - 1, -1):
			l += A[i]
			if l > llocalmax:
				llocalmax = l
		r = 0; rlocalmax = A[mid+1];
		for i in range(mid+1, q + 1):
			r += A[i]
			if r > rlocalmax:
				rlocalmax = r
		print "lmax = %s rmax = %s llocalmax = %s rlocalmax = %s" %(lmax, rmax, llocalmax, rlocalmax)
		return max(lmax, rmax, llocalmax + rlocalmax)

print max_sum_subarray([9, -7, 5, -2, 5, -7, 8, -9], 0, 7)
		