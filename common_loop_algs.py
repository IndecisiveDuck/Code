#Sum and average of a sequence of numbers
print("Enter numbers... q to quit")
ev_count = 0
od_count = 0
while True:
    text_in = input()
    if text_in == "q":
        break
    n = int(text_in)
    if n % 2 == 0:
        ev_count += 1
    else:
        od_count += 1

print(f"You have {ev_count} even numbers and {od_count} odd numbers")
#couting matches APPLES AND ORANGES 
# finding the median, mean, sorting