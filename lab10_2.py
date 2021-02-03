
''' Write a program that accepts an integer from user and raises ValueError 
with argument ‘Abnormal Condition’, if the reading is not within 90 – 120. '''

try:
  n = int(input("Enter a number between 90 and 120:\t"))
  if n < 90 or n >120:
    raise ValueError('Abnormal Condition')
except ValueError as ve:
  print(ve)