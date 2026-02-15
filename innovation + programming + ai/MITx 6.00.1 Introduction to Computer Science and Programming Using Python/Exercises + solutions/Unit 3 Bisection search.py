
# ========================================
# unit 3 exercises + solutions
# bisection search
# ========================================


# ----- bisection search -----

# guess my number


low = 1
high = 99
guess = (high + low)//2


print("Please think of a number between 0 and 100!")
print("Is your secret number", guess, " ?")
hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while hint != "c":
    if hint == "l":
        low = guess + 1
    elif hint == "h":
        high = guess - 1
    else: print("Sorry, I did not understand your input.")
  
    
    guess = int((high + low)//2)
    print("Is your secret number", guess, " ?")
    hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
if hint == "c":
    print("Game over. Your secret number was: ", guess, ".")
