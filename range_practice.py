number = 16
for a in range (1, number+1):
    for b in range(1, number+1):
        print(a*b, end=" ")
        if b == number:
            print()