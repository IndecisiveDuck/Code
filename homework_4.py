import random
#Rock paper scisors

def leap_year_funtion():
    given_year = int(input("Enter a year: "))
    if given_year > 1582 and given_year % 4 == 0 and (not given_year%100==0 or given_year%400==0):
        return "is"
    else:
        return "is NOT"
    
options = ["ROCK", "PAPER", "SCISSORS"]
computer_choice = random.choice(options)
player_choice = input("Rock paper or scissors? ").upper()

if player_choice in options:
    if player_choice == computer_choice:
        result = 0
    elif ((player_choice == "ROCK" and computer_choice == "PAPER") or
         (player_choice == "PAPER" and computer_choice == "SCISSORS") or
         (player_choice == "SCISSORS" and computer_choice == "ROCK")):
        result = 1
    elif ((player_choice == "SCISSORS" and computer_choice == "PAPER") or
         (player_choice == "ROCK" and computer_choice == "SCISSORS") or
         (player_choice == "PAPER" and computer_choice == "ROCK")):
        result = 2
else:
    print("Invalid choice option!")

result_type = ['tie', 'lose', 'win']

print(f"Computer chooses {computer_choice}")
print(f"You {result_type[result]}")

#Write a program that asks the user for a year and 
# computes whether that year is a leap year. As an extension, 
# see if you can do this with a single if statement without nesting. 
# You should do the following tests:

months_with_30_days = ["september", "april", "june", "november"]
months_with_31_days = ["january", "march", "may", "july", "august", "october", "december"]
given_month = input("Enter a month: ")

if given_month.lower() in months_with_30_days:
    print(f"{given_month} has 30 days")
elif given_month.lower() in months_with_31_days:
    print(f"{given_month} has 31 days")
elif given_month.lower() == "febuary":
    reson = leap_year_funtion()
    print(f"{given_month} {reson} a leap year.")
    if reson == "is NOT":
        print(f"{given_month} has 28 days")
    else:
        print(f"{given_month} has 29 days")