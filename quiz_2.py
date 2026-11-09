# Write a function months_to_savings_goal that takes the following inputs:

# goal - the savings target
# monthly_contribution - the amount of money added to the account at the beginning of each month
# interest_rate - monthly interest rate, expressed as a percent (so 5.0 for 5%).
# and calculates the number of months to reach or exceed the goal. For example, 
# months_to_savings_goal(5000, 100, 0.2) should return 48 (because of interest earned, 
# the goal is reached two months earlier than it would be based on contributions alone).

# Include type hints and a docstring in your solution.

# The goal and monthly savings contribution must be > 0 and the interest rate must be >= 0. 
# If an illegal value is used, return -1.

def months_to_savings_goal(goal:float, monthly_contribution: float, interest_rate: float) -> int:
    """Takes the users input and calculates how long it will take for them to reach their savings goal.

    Args:
        goal (float): How much the user wants to save
        monthly_contribution (float): How much mony is being added to the savings per month. Must be greater than zero
        interest_rate (float): The interest rate of the account, must be greater than or equal to zero

    Returns:
        int: The amount of months it takes for the total to match or be greater than their goal. If invalid inputs, returns -1
    """
    if monthly_contribution <= 0 or interest_rate < 0:
        return -1

    total = 0
    count = 0
    while total < goal:
        total += monthly_contribution
        total += (total*interest_rate/100)
        count += 1

    return count

def main():
    goal = float(input("What is your savings goal? $"))
    contribute = float(input("How much do you contribue monthly? $"))
    rate = float(input("What is your interest rate? "))
    print(months_to_savings_goal(goal, contribute, rate))

main()