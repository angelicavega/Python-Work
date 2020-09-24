#Here we take the input value from the user
outstanding_balance = float(input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(input('Enter the annual credit card interest rate as a decimal:'))
minimum_monthly_payment_rate = float(input('Enter the minimum monthly payment rate as a decimal:'))

#Here we define a function using the variables
def compute_debt():
  for x in range(1,13):
    minimum_monthly_payment = minimum_monthly_payment_rate*outstanding_balance
    interest_paid = annual_interest_rate/12*outstanding_balance
    principle_paid = minimum_monthly_payment-interest_paid
    remaining_balance = outstanding_balance-(principle_paid+minimum_monthly_payment)
    print('Month:', x )
    print('Minimum monthly payment:', minimum_monthly_payment)
    print('Principle paid:', principle_paid)
    print('Remaining balance:', remaining_balance)

#Here we call the function
compute_debt()

