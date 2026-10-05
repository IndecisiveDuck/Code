#calculate how much of each USD currency the tester has by their given amount of change
change = int(input("How much change do you have? "))
DOLLARS = 100
QUARTER = 25
DIMES = 10
NICKELS = 5
coins_amount = [DOLLARS, QUARTER, DIMES, NICKELS]
total_coins = [0,0,0,0]
change_remaining = 0

for index, coins in enumerate(coins_amount):
    if index == 0:
        total_coins[index] = change // coins
        change_remaining = change % coins
    else:
        total_coins[index] = change_remaining // coins
        change_remaining = change_remaining % coins

print(f"Dollars:{total_coins[0]} Quarters:{total_coins[1]} Dimes:{total_coins[2]} Nickles:{total_coins[3]} Pennys:{change_remaining}")