"""
This is a program to make an imputed string into camelCase
"""
#get user string input and split into list
userString = input('Please enter a string with more than one word seperated by spaces: ').lower().split()

out = '' #empty string, appened words go into

for userString in userString:
	titleCased = userString.title() #title function puts first letter as capital
	out += titleCased


# lowercase the first letter
out = out[0].lower() + out[1:] #string index
#print camelCase
print(out)