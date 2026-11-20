def paycheck_amount(hourly_wage: float, hours_worked: float)-> float:
    """Calculates the weeksly pay based on wage and hours worked. If someone
    works more than 40 hours per week, they are paid time and a half for those
    extra hours.

    Args:
        hourly_wage (float): must be greater than 0
        hours_worked (float): must be greater than 0 and less than 168

    Returns:
        float: the weekly paycheck amount. Raises error if invalid inputs
    """
    if not isinstance(hourly_wage, float) and not isinstance(hourly_wage, int):
        raise TypeError
    if not isinstance(hours_worked, float) and not isinstance(hours_worked, int):
        raise TypeError
    if hours_worked < 0 and hours_worked >= 168:
        raise ValueError(f"Invalid hourly_wage: {hourly_wage}")
    if hourly_wage <= 0:
        raise ValueError(f"Get a job that pays better")
    total = 0
    basepay = hours_worked * hourly_wage
    if hours_worked > 40:
        overtime = 0.5 * (hours_worked - 40)
        total = basepay + overtime

    return total

def main():
    pay = float(input("Enter hourly wage: "))
    hours = float(input("Enter Hours worked: "))
    print(paycheck_amount(pay, hours))

main()
