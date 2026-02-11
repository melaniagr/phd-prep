
# ========================================
# unit 2 exercises + solutions
# core elements | loops 
# ========================================

# # ----- hello world -----  

# Write a piece of Python code that prints out the string hello world

print("hello world")



# ----- happy -----  

# Write a piece of Python code that prints out the string 'hello world' if the value of an integer variable, happy, is strictly greater than 2.

if happy > 2:
    print("hello world")



# ----- while -----  

# In this problem you'll be given a chance to practice writing some while loops.

# Convert the following into code that uses a while loop.

# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!


m = 2
while m < 11:
    print(m)
    m = m + 2
if m > 10:
    print("Goodbye!")


# ----- for -----  

# In this problem you'll be given a chance to practice writing some for loops.

# Convert the following code into code that uses a for loop.

# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

for i in range(2,12,2):
    print(i)
    if i == 10:
        print("Goodbye!")
