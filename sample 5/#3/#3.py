''' Write a program that accepts two numbers from user and perform
addition, subtraction, multiplication and division of numbers using
functions available in each module '''

import arithmetic.add as add
from arithmetic.sub import sub
from arithmetic.carithmetic import *

try:
	x = int(input("Enter first number:\t"))
	y = int(input("Enter second number:\t"))

	print(x," + ",y," =\t", add.add(x,y))
	print(x," - ",y," =\t", sub(x,y))
	print(x," * ",y," =\t", mul(x,y))
	if div(x,y) != None:
		print(x," / ",y," =\t", div(x,y))

except ValueError as ve:
	print(ve)