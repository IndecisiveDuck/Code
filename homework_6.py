#Nim is a well-known game with a number of variants. The following variant has an interesting winning strategy: 
import random
# Two players alternately take marbles from a pile.
# In each move, a player chooses how many marbles to take.
# The player must take at least one but at most half of the marbles.
# Then the other player takes a turn.
# The player who takes the last marble loses.

#Write a program in which the computer plays against a human opponent. 
# Generate a random integer between 10 and 100 to denote the initial size of the pile. 
# Randomly decide whether the computer or the human takes the first turn. The computer simply 
# takes a random legal value (between 1 and n/2) from the pile whenever it has a turn, whereas 
# the human player can choose how many marbles to take. Ensure that the human player is not 
# allowed to make an invalid move! If you have the first move, there is a strategy you can use 
# so that you will (almost) never lose. See if you can figure it out! Here is a sample run of me 
# playing against the computer:
marble_piles = random.randint(10, 100)
star = random.randint(0,1)
while marble_piles > 1:
    print(f"{marble_piles} marbles remaining...")
    while not star == 1:
        player_takes = input("How many marbles would you like to take? ")
        if not player_takes.isdigit() or int(player_takes) < 1 or int(player_takes) > marble_piles//2:
            print("Invalid move, please choose a value betewen 1 and "+str(marble_piles//2))
        else:
            player_takes = int(player_takes)
            marble_piles -= player_takes
            star = 1
    if marble_piles == 1:
        print("You won!")
        break
    elif star == 0:
        print(f"{marble_piles} marbles remaining...")
    computer_takes = random.randint(1, marble_piles//2)
    marble_piles -= computer_takes
    print(f"Computer takes {computer_takes} marbles")
    if marble_piles == 1:
        print("You lose")
        break
    star = 0


#retirement
age = int(input("What is your current age? "))
retire_age = int(input("What age do you what to retire? "))
investment = float(input("How much money will you save each year for retirement? $"))
retirement_goal = float(input("What is your retirement savings goal? $"))
count_all = 0
count_reire = 0
for i in range(1000):
    rate = random.random()
    while age < retire_age:
        # Randomize what the rate of return is for this year
        returns = investment*(rate/100)
        investment += returns
        age += 1
    #print (f"Age {age}: Balance: ${investment:,.2f}, annual investment returns: ${returns:,.2f}")
    print(f"Trial {i}, final balance ${investment:,.2f}")
    count_all +=1
    if investment > retirement_goal:
        count_reire += 1
precent = count_reire/count_all
print(f"You met your goal %{precent} precent of the time!")

# #Checkerboard
# while True:
#     n = int(input("Enter board size: "))
#     if n > 1:
#         break
#     else:
#         print("Invalid input")

# for a in range (1, n+1):
#     if a%2 == 0:
#         print("# "*4)
#     else:
#         print(" #"*4)