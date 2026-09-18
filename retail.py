change = 123
DOLLARS = 100
QUARTER = 25
DIMES = 10
NICKELS = 5
n_dollars = change // DOLLARS
change_remaining = change % DOLLARS
n_quarters =  change_remaining // QUARTER #int after division
change_remaining = change_remaining % QUARTER #remainder after division
n_dimes = change_remaining // DIMES
change_remaining = change_remaining % DIMES
n_nickles = change_remaining // NICKELS
change_remaining = change_remaining % NICKELS
pennys = change_remaining % NICKELS

print(f"Dollars:{n_dollars} Quarters:{n_quarters} Dimes:{n_dimes} Nickles:{n_nickles} Pennys:{pennys}")