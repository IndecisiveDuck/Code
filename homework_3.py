import random
#An online retailer offers a discount of 40% if a customer purchases $100 or more of merchandise. 
#Write a program that will tell the user what if they receive the discount what their 
# new bill is or how much more they need to purchase to receive the discount.

spenting = float(input("How much did you spend? $"))

if spenting < 100:
    print("You are not eligible to receive a discount :-(")
    how_much_more_needed = 100.00 - spenting
    print(f"Please purchase an additional ${how_much_more_needed:.2f} to recieve your discount.")
else:
    discount_price = spenting - (spenting * (40/100))
    print("You are eligible for a discount!")
    print(f"Your total is now ${discount_price:.2f}")


#Write a program that asks for the current temperature and then prints a humorous description 
# of what HACTC students do at that temperature.

tempeture = float(input("Enter temperature in degrees F: "))

if tempeture < 40:
    print(f"The software engineering students will burn the supply closet for warmth and abandon their weakest link (Linkon) if left in {tempeture} weather for more than 3 hours")
elif tempeture < 70:
    print(f"Software engineering students will be happy as long as they are provided food. If food is not provided they will congragate to summon a long forgotten diety with Mulloy and Alex(Maybe Alex) as a sacrafice.")
elif tempeture < 90:
    print(f"Software students will make icecream appear. We don't know how, it just showed up.")
else:
    print("Software students did not show up because they are too busy fighting the zombie apocolipse. They have made a new society in the waste land within Linkon's manor. With Morgen and Linkon as reluntcant co-op leadership, Willam as the rebellion leader who Linkon kicks out because of his democratic will.")


#Write a program that plays rock-paper-scissors against the computer. The user should enter 
# their choice and the computer should choose randomly using this line of code:

options = ["ROCK", "PAPER", "SCISSORS"]
computer_choice = random.choice(options)
player_choice = input("Rock paper or scissors? ").upper()

if player_choice in options:
    if player_choice == "ROCK":
        if computer_choice == "ROCK":
            result = 0
        elif computer_choice == "PAPER":
            result = 1
        else:
            result = 2
    elif player_choice == "PAPER":
        if computer_choice == "ROCK":
            result = 2
        elif computer_choice == "PAPER":
            result = 0
        else:
            result = 1
    else:
        if computer_choice == "ROCK":
            result = 1
        elif computer_choice == "PAPER":
            result = 2
        else:
            result = 0
else:
    print("Invalid choice option!")

result_type = ['tie', 'lose', 'win']

print(f"Computer chooses {computer_choice}")
print(f"You {result_type[result]}")