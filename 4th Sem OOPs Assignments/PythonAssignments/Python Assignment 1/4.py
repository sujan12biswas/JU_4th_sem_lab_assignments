# Write a regular expression to validate a phone number.
import re

def isValid(s):
	
	# 1) Begins with 0 or 91
	# 2) Then contains 6 or7 or 8 or 9.
	# 3) Then contains 9 digits
	Pattern = re.compile("(0/91)?[6-9][0-9]{9}")
	return Pattern.match(s)

# Driver Code
s = (input("Enter Mobile Number: ")) 
if (isValid(s)):
	print ("Valid Number")	
else :
	print ("Invalid Number")
