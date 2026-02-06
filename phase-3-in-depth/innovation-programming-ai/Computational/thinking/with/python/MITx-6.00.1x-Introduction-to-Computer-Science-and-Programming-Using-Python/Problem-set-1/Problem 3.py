
# Problem 3

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s 
# in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh


# In the case of ties, print the first substring. 
# For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc



max_largo = 1
current_largo = 1
posicion = s[0:1]

for i in range(len(s)-1):
    noinfinito = 0
    while i + noinfinito + 1 < len(s) and ord(s[i + noinfinito]) <= ord(s[i+noinfinito+1]):       
        current_largo += 1
        noinfinito += 1
        if current_largo > max_largo:
            max_largo = current_largo
            posicion = s[i:(i+max_largo)]
    current_largo = 1
        
print("Longest substring in alphabetical order is: ", posicion)