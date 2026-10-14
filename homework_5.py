#Make a guessing game that asks the user to guess a randomly chosen number 
# between 0 and 100 and tells them if their guess is too high or too low.

import random

number=random.randint(0,100)
guess = False

while guess != number:
    guess = input("Guess a number between 0 and 100: ")
    if guess.isdigit():
        guess = int(guess)
        if guess > number:
            print("Too High!")
        elif guess < number:
            print("Too Low!")
        elif guess == number:
            print("Correct!")
            break
    else:
        print("Invalid input!")

#Write an application to pre-sell a limited number of cinema tickets. 
# Each buyer can buy as many as 10 tickets. No more than 50 tickets can be sold. 
# Implement a program that prompts the user for the desired number of tickets and then displays 
# the number of remaining tickets. For each order, you need to check that:

#the order is not above the max purchase size of 10,
#there are enough tickets left to fulfill the order, and
#the order size is positive.

print("Welcome to Entertainment cinemas!")
n_tickets = 50
customer_count = 0
while n_tickets > 0:
    purchace_size = int(input("How many tickets would you like to buy? "))
    if purchace_size < n_tickets and purchace_size <= 10:
        print("Enjoy the show!")
        customer_count += 1
        n_tickets -= purchace_size
    elif purchace_size > 10:
        print("Sorry, the max order size is 10 tickets")
    else:
        print("Sold out!")
        print(f"There were {customer_count} customers")
        break

    print(f"We have {n_tickets} ticket(s) remaining.")

#retirement calculator

age = int(input("What is your current age? "))
retire_age = int(input("What age do you what to retire? "))
investment = float(input("How much money will you save each year for retirement? $"))

while age < retire_age:
    returns = investment*(9.62/100)
    investment += returns
    age += 1
    print (f"Age {age}: Balance: ${investment:,.2f}, annual investment returns: ${returns:,.2f}")