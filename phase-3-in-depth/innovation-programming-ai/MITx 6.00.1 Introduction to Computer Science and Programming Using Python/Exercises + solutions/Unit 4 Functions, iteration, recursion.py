
# ========================================
# unit 4 exercises + solutions
# functions | iteration | recursion
# ========================================

# ============= functions ======================

# ----- square -----  

# Write a Python function, square, that takes in one number and returns the square of that number.
# This function takes in one number and returns one number.


def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    return x**2



# eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a*(x**2)+b*x+c

# This function takes in four numbers and returns a single number.

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*(x**2) + b*x + c


# ----- fourth power ----- 

# Write a Python function, fourthPower, that takes in one number 
# and returns that value raised to the fourth power.

# You should use the square procedure that you defined in an earlier exercise.

# This function takes in one number and returns one number.

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))


# ----- odd ----- 

# Write a Python function, odd, that takes in one number 
# and returns True when the number is odd and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    if x % 2 == 0:
        return False
    else: 
        return True



# ============= iterations and recursions ======================

# ----- iter power ----- 

# Write an iterative function iterPower(base, exp) that calculates the exponential base^exp
# by simply using successive multiplication. For example, iterPower(base, exp) 
# should compute base^exp by multiplying base times itself exp times. 
# Write such a function below.

# This function should take in two values - base can be a float or an integer; 
# exp will be an integer  0. It should return one numerical value. 
# Your code must be iterative - use of the ** operator is not allowed.



def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = base
    if exp == 0:
        result = 1
    else:
        for i in range(exp-1):
            result = result*base

    return result



# ----- power recur ----- 


# In Problem 1, we computed an exponential by iteratively executing successive 
# multiplications. We can use the same idea, but in a recursive function.

# Write a function recurPower(base, exp) which computes base^exp by recursively calling itself 
# to solve a smaller version of the same problem, and then multiplying the result by 
# base to solve the initial problem.

# This function should take in two values - base can be a float or an integer; 
# exp will be an integer . 
# It should return one numerical value. 
# Your code must be recursive - use of the ** operator or looping constructs is not allowed.

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    result = base
    
    if exp == 0:
        result = 1
    elif exp == 1:
        result = base
    else:
        result = result*recurPower(base, exp-1)
    return result 



# ----- gcd iter ----- 

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # define menor, mayor
    
    if a <= b:
        menor, mayor = a, b
    else:
        menor, mayor = b, a
    
    # look for gcd
    
    menor2 = menor
    
    while mayor % menor != 0:        # keep going until divisible (mayor / menor)
        menor -= 1                   # stops when divisible, hence menor = gcd
        while menor2 % menor != 0:   # keep going until divisible (original menor/ current menor)
            menor -= 1
    return menor




# ----- gcd Recur ----- 

# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

# If b = 0, then the answer is a

# Otherwise, gcd(a, b) is the same as gcd(b, a % b)

# Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # define menor, mayor
    
    menor, mayor = min(a, b), max(a,b)
    
    if mayor % menor == 0:
        return menor
    else:
        return gcdRecur (menor, mayor % menor)




# ----- is In ----- 

# We can use the idea of bisection search to determine if a character is in a string, 
# so long as the string is sorted in alphabetical order.

# First, test the middle character of a string 
# against the character you're looking for (the "test character"). 
# If they are the same, we are done - we've found the character we're looking for!

# If they're not the same, 
# check if the test character is "smaller" than the middle character. 
# If so, we need only consider the lower half of the string; 
# otherwise, we only consider the upper half of the string. 
# (Note that you can compare charac ters using Python's < function.)

# Implement the function isIn(char, aStr) 
# which implements the above idea recursively to test if char is in aStr. 
# char will be a single character and aStr will be a string that is in alphabetical order.
# The function should return a boolean value.


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:                
        return False
    elif len(aStr) == 1 and char == aStr:
        return True
    elif len(aStr) == 1 and char != aStr:
        return False
    else:
        middlechar = aStr[(len(aStr))//2]       # 1. test middle 
        if char == middlechar:
            return True        
        elif char < middlechar:             # is char smaller? then again
            aStr = aStr[:(len(aStr))//2]
            return isIn(char, aStr)
        elif char > middlechar:             # is char bigger? then again
            aStr = aStr[(len(aStr))//2:]        
            return isIn(char, aStr)
