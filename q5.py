def smallest_multiple(count):
	k = 0
	while k != 20:
		for i in range(1, 21):
			if count % i == 0:
				k = k + 1
			else: 
				k = 0
				count = count + 1
	return count