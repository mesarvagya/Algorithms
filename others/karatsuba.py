x = 1234567812345678123456781234567812345678
y = 9876543298765432987654329876543298765432

def karatsuba(x,y):
	if(len(str(x)) == 1 or len(str(y)) == 1):
		# Single digit number can be easily solved. Just multiply and return. It is also our base case.
		return x*y

	str_x = str(x)
	str_y = str(y)

	n = max(len(str_x),len(str_y))

	mid = n/2

	a = x/ (10**mid)
	b = x % (10 ** mid)

	c = y/ (10**mid)
	d = y % (10 ** mid)

	ac = karatsuba(a,c) # recursively compute ac
	bd = karatsuba(b,d) # recursively compute bd
	ad_plus_bc = karatsuba(a+b, c+d) - ac - bd # find ad+bc using the trick of (a+b)(c+d)-ac-bd

	product = ac * (10 ** (2*mid)) + ad_plus_bc * (10 ** mid) + bd
	return product

print karatsuba(x,y)