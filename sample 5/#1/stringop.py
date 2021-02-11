# Module stringop


import string
# a) Function to reverse string
def reverseString(s):
	return s[::-1]




# b) Function to determine the number of uppercase letters and lowercase letters in a string
def countUpperAndLower(s):
	lowercaseCount, uppercaseCount = 0,0
	for x in s:
		if x in string.ascii_lowercase:
			lowercaseCount += 1
		else:
			if x in string.ascii_uppercase:
				uppercaseCount += 1
	return uppercaseCount, lowercaseCount




# c) Function to check whether a string is palindrome
def checkPallindrome(s):
	if s == s[::-1]:
		return True
	else: return False




# d) Function to check whether a string is a pangram
# (Pangrams are words or sentence containing every letter of the alphabet at least once)
# Eg: The quick brown Fox Jumps over a lazy Dog
def checkPangram(s):
	for x in string.ascii_lowercase:
		if x in s.lower():
			continue
		else:
			return False
	else:
		return True