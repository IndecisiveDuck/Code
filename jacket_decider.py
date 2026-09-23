#this program helps you decide if you need to wear a jacket
#if it is cold, wear a jacket when it is cold (below 50) or when it is raining

#promt the user for the current tempature
#ask the user if it is raining, print out if they need a jacket

jacket_tempeture = int(input("What is the tempeture outside(F)? "))
is_raining = input("is it raining outside (Y/N)? ").upper() == "Y"

if jacket_tempeture < 50 or is_raining:
    print("Yeah, you should wear a jacket")
else:
    print("No, you odn't need a jacket")