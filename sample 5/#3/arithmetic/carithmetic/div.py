#Module div

def div(x,y):
	try:
		return x/y
	except ZeroDivisionError as e:
		print("Division: Please enter a non-zero divisor.")