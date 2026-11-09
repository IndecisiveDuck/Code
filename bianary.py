
def bianary_loop(number: int):
    if number == 0:
        return ""

    return bianary_loop(number//2) + str(number%2)

print(bianary_loop(13))

def digit_sum(number:int):
    if number == 0:
        return 0

    return number%10 + digit_sum(number//10)

print(digit_sum(1701))