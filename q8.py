from functools import reduce

def greatest_product(n):
	
	def product(a, b):
		return a * b

	a = str(n)
	products = list()
	x, y = 0, 5
	while y <= len(a):
		current = list()
		for i in range(x, y):
			current.append(a[i])
		products.append(reduce(product, map(int, current)))
		x += 1
		y += 1
	return max(products)