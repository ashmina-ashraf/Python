'''Write example program to demonstrate Chained exception, re- raised exception and AssertError (self-study) in Python.'''


try:
  print("Division:\n")
  a = int(input("Enter an even number:\t"))
  assert (a%2==0), 'Divident must be even'                          #Assertion
  
  try:
    b = int(input("Enter Divisor:\t"))
    print("Result:\t",a/b)
  except ZeroDivisionError as e:
    raise IOError('Divisor cannot be 0') from ZeroDivisionError     #Chained Exception
  except ValueError as ve:
    print('From Inner block')   
    raise                                                           #Re-raised Exception

except IOError as ioe:
  print("Chained Exception:\t",ioe)
except AssertionError as ae:
  print(ae)
except ValueError as ve:
  print('Enter an integer')
