#In Pokemon, Charmander evolves into Charmeleon at level 16 and into Charizard at level 36. 
# Write a program that asks the user to input a level and prints out what Pokemon
#  of this species results.

char_level = int(input("What level is your fire type starter? "))

if char_level < 16:
    char_evolution = "Charmander"
elif char_level < 36:
    char_evolution = "Charmeleon"
else:
    char_evolution = "Charizard"

print(f"You have a level {char_level} {char_evolution}")