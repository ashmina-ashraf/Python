''' Write a program that imports ‘stringop’ and perform the above functions
on a string entered by user.'''

import stringop

string = input("Enter a string:\t")
print("\n\na) Reversed String:\t",stringop.reverseString(string))

uppercase,lowercase = stringop.countUpperAndLower(string)
print("\nb) Uppercase letters: \t",uppercase,"\n   Lowercase letters:\t",lowercase)

print("\nc) Is pallindrome?:\t",stringop.checkPallindrome(string))

print("\nd) Is pangram?:\t",stringop.checkPangram(string))