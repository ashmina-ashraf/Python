'''Write a custom exception which is raised if user entered login credentials remain invalid.'''


class PasswordError(Exception): pass

try:
  password = input("Enter your password:\t")
  if password != 'admin':
    raise PasswordError("Password you entered is incorrect. Try Again!")
  else:
    print("\nWelcome!")
except PasswordError as pe:
  print(pe)