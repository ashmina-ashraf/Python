# Write a program to demonstrate ZeroDivisionError and ValueError

print("\tDIVISION\n")
try:
  a = int(input("Enter Divident:\t"))
  b = int(input("Enter divisor:\t"))
  print("\nResult:\t",a/b)
except ZeroDivisionError  as zde:
  print("\nDivision by zero is not defined. Please enter a non-zero divisor.")
except ValueError as ve:
  print("\nPlease enter an integer value.")