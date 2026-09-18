#ask the user to input their hourly wage, and number of hours worked in a week
hourly_wage = float(input("Enter your hourly wage: $"))
hours_worked = float(input("How many hours did you work this week? "))

FULL_TIME_HOURS = 40

#see if we need to add overtime
if hours_worked < 40:
    
    overtime_pay = (hours_worked - 40) * hourly_wage / 2
    paycheck_amount = paycheck_amount + overtime_pay
else:
    #program will print out their paycheck amount
    paycheck_amount = hourly_wage * hourly_wage

print(f"Your paycheck this week is ${paycheck_amount:,.2f}")