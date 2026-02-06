# Problem 1

# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid # vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5

numvowels = 0
for vowels in s:
    if vowels == "a" or vowels == "e" or vowels == "i" or vowels == "o" or vowels == "u":
        numvowels += 1
        
print("Number of vowels: " + str(numvowels))