import math

def largest_prime_factor(n):
	def factor(x):
		if x <100000000:
			factors = list()
			for i in range(1, x + 1):
				if x % i == 0:
					factors.append(i)
			return factors
		factors = list()
		for i in range(1, x // (10 ** ((math.floor(math.log10(x))) - 6))  + 1):
			if x % i == 0:
				factors.append(i)
		return factors

	def prime(y):
		factors = list()
		counter = 0
		for i in range(1, y + 1):
			if y % i == 0:
				factors.append(i)
				counter = counter + 1
			if counter > 2:
				return False
		return True

	return(max(filter(prime, factor(n))))