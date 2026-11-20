#The program asks the user for two int and then reports their quotient
while True:
    try:
        a = int(input("Enter the numerator: "))
        break
    except ValueError:
        print("Please input an integer")
while True:
    try:
        b = int(input("Enter the denominator: "))

        q = a / b
        print("The quotent is", q)
    except ValueError:
        print("Please input an integer")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    
