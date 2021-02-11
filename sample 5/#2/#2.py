''' Write a program that imports ‘listop’ and perform above functions on a user
input list. '''

import listop

try:
	list1 = list(map(int, input("Enter a list of integers:\t").split()))

	print("\n\na) After removing duplicates:\t",listop.removeDuplicates(list1))
	print("\nb) New list with squares of elements:\t",listop.squareofLitElements(list1))

except ValueError as ve:
	print("\nPlease enter integers")