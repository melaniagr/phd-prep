# problem 2

# data given

balance = 3329
annualInterestRate = 0.2

# variables I will use

minimumfixedmonthlypayment = balance     # define for initial iteration

monthlyinterestrate = annualInterestRate/12.0
monthlyunpaidbalance = balance - minimumfixedmonthlypayment
updatedbalanceeachmonth = monthlyunpaidbalance + monthlyinterestrate*monthlyunpaidbalance


minimumfixedmonthlypayment = balance - 1  

while balance > 0 or balance <-9 :
	for i in range(1,13):
		monthlyinterestrate = annualInterestRate/12.0
		monthlyunpaidbalance = balance - minimumfixedmonthlypayment
		updatedbalanceeachmonth = monthlyunpaidbalance + monthlyinterestrate*monthlyunpaidbalance
		balance = updatedbalanceeachmonth
		minimumfixedmonthlypayment -= 10
print(minimumfixedmonthlypayment)


lowestpayment10 = round(((minimumfixedmonthlypayment+1)/10)*10)     # redondeo hacia arriba

print("Lowest Payment: ", lowestpayment10)     # things i need to print by the end




def lowestpayment(balance, annualInterestRate) :
    '''
    given balance and annualInterestRate = 0.2
    returns the lowest fixed payment possible to pay debt

    '''
    



bisection con otra

def lowestpayment((1+balance/12)/2), balance, annualInterestRate):
    '''
    dadas esas dos variables, encontrar el fixed lowest payment posible
    '''
    
    low = 1
    high = balance/12
    guesspayment = (high + low)//2
    monthlyinterestrate = annualInterestRate/12.0
 
    for i in range(12):
        monthlyunpaidbalance = balance - guesspayment
        updatedbalanceeachmonth = monthlyunpaidbalance + monthlyinterestrate*monthlyunpaidbalance

        if guesspayment*12 <= updatedbalanceeachmonth:
            if guesspayment*12 <= updatedbalanceeachmonth/2:
                low = guesspayment + 1
                return lowestpayment()
            else:
                high = guesspayment - 1
        elif guesspayment*12 > updatedbalanceeachmonth:
            return print("Lowest Payment: ", round(((guesspayment+1)/10)*10))     # # redondeo hacia arriba, things i need to print by the end
        
            
