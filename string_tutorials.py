cringe = input("Does this string contain only numbers and letters? ").isalnum()
print(cringe)
if cringe:
    print("this string contains only numbers and letters")
else:
    print("This string has more than just numbers and letters")

alpha = input("Does this string contain only letters? ").isalpha()
print(alpha)
if alpha:
    print("this string contains only letters")
else:
    print("this string contains more than just letters")

digit = input("Does this string only contain numbers? ").isdigit()
print(digit)
if digit:
    print("this string contains only numbers")
else:
    print("this string contains more than just numbers")

orange_juice = input("Does this string have all lower case letters? ").islower()
print(orange_juice)
if orange_juice:
    print("this string contains only lower case characters")
else:
    print("this string contains more than just lower case letters")

jupiter = input("Does this consist of only spaces, enters, or tabs? ").isspace()
print(jupiter)
if jupiter:
    print("this string contains only whitespace")
else:
    print("this string contains more than just whitespace")

cabbage = input("Does this string contain only upper case characters? ").isupper()
print(cabbage)
if cabbage:
    print("this string contains only upper case characters")
else:
    print("this string contains more than just upper case characters")