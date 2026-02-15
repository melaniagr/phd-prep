
# problem 2
# given balance and annualinterestrate

currentbalance = balance
payment = ((balance/12)//10)*10 -10    

# minimumfixedmonthlypayment = payment
while True:
    currentbalance = balance
    for i in range(12):
        updatedbalanceeachmonth = (currentbalance - payment)  + (annualInterestRate / 12.0)*(currentbalance - payment)
        currentbalance = updatedbalanceeachmonth
    if currentbalance <= 0:
         break
    payment += 10
    
print("Lowest Payment: ", int(payment))
