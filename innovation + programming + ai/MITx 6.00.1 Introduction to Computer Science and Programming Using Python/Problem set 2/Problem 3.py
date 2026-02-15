# problem 3

# given: 
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

monthlyinterestrate = annualInterestRate / 12.0
lower = balance / 12                                            # Monthly payment lower bound
upper = (balance*(1 + monthlyinterestrate)**12) / 12.0          # Monthly payment upper bound
epsilon = 0.01                                                       # to the cent
payment = (lower + upper)/2.0                                 # payment ~ guess
currentbalance = balance

while abs(currentbalance) > epsilon:
    currentbalance = balance
    for i in range(12):
        updatedbalanceeachmonth = (currentbalance - payment)  + (annualInterestRate / 12.0)*(currentbalance - payment)
        currentbalance = updatedbalanceeachmonth
    if currentbalance > epsilon:                 # still have balance to pay at the end of the year
        lower = payment
    elif currentbalance < -0.01:                                    # paid before the year ends                     
    	upper = payment
    payment = (lower + upper)/2.0    
    
print("Lowest Payment: ", round(payment, 2))