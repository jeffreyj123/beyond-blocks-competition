from functools import reduce

def add(x , y):
	return x + y

def even_fib_not_exceeding(n):
	even_fib=list()
	pred, curr = 0, 1
	while curr < n:
		pred, curr = curr, pred + curr
		if curr % 2 == 0:
			even_fib.append(curr)
	return reduce(add, even_fib)