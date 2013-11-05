def prime_number(n):
	k = 0
	count = 3
	prime = [2]
	while len(prime) != n:
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
	return prime[n - 1]