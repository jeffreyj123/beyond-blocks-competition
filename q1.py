from functools import reduce

def add (x , y):
	return x + y

def multiples_3_5(n):
	k=1
	terms=list()
	while k<n:
		if k % 3 == 0 or k % 5 == 0:
			terms.append(k)
		k = k + 1
	return reduce(add, terms)