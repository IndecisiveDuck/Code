# def is_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return "not"
#     return ""
# while True:
#     number = int(input("Enter a number: ")), print(f"{number} is {is_prime(number)} a prime number")
def leap_year_funtion(given_year):
    if given_year > 1582 and given_year % 4 == 0 and (not given_year%100==0 or given_year%400==0):
        return 366
    else:
        return 365

def month_fun(now_month_n, then_month_n):
    months_with_30_days = [9, 4, 6, 11]
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    for a in range(then_month_n, 12):
        if then_month_n in months_with_30_days:
            months_days += 30
        elif then_month_n.lower() in months_with_31_days:
            months_days += 31
elif then_month_n.lower() == "febuary":
    reson = leap_year_funtion()
    print(f"{then_month_n} {reson} a leap year.")
    if reson == "is NOT":
        print(f"{then_month_n} has 28 days")
    else:
        print(f"{then_month_n} has 29 days")

    
def days_elapsed(now_year, then_year):
    years_days = 0
    years = now_year - then_year
    for i in range(1, years):
        years_days += leap_year_funtion(then_year+i)



print(days_elapsed(2026, 2009))