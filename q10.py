from functools import reduce

def add(x, y):
	return x + y

def prime_sum(n):
	k = 0
	count = 3
	prime = [2]
	while count <= n:
		for i in range (0, len(prime)):
			if  count % prime[i] != 0:
				k = k + 1
				if k == len(prime):
					prime.append(count)
					count = count + 1
					k = 0
			else: 
				k = 0
				count = count + 1
	return reduce(add, prime)