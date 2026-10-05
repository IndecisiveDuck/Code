# Program will tell us how long it will take to pay off a loan
# ask user for loan amount, interest ratem monthly payement
# program will report how long it will take to pay off loan

loan_amount = float(input("How much money did you borrow? "))
interest_rate = float(input("What is the interest rate of the loan? "))
monthly_payment = float(input("How much are you paying towards your loan? "))

n_payments = 0
balance = loan_amount
while monthly_payment < interest_rate *loan_amount / 1200:
    print("Insufficent Payement amount!")
    monthly_payment = float(input("How much are you paying towards your loan? "))
    
while balance > 0:
    interest = balance * interest_rate / 1200
    balance = balance + interest - monthly_payment
    n_payments = n_payments + 1
    print(f"balance = ${balance:,.2f}")

print(f"it took {n_payments} month(s) to pay off")