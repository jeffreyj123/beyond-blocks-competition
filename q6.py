from functools import reduce

def sum_square_difference(end):
	
	def add(a, b):
		return a + b

	def square(c):
		return c **2

	def sum_squares(d):
		squares = list()
		for i in range (1, d + 1):
			squares.append(i**2)
		return reduce(add, squares)

	def squares_of_sum(e):
		nat_sum = list()
		for i in range (1, e + 1):
			nat_sum.append(i)
		return square(reduce(add, nat_sum))

	return (squares_of_sum(end) - sum_squares(end))