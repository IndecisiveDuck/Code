string = "Linkon is a loser"
vowels = ["a", "e", "i", "o", "u", "y"]
count =0

for letters in string:
    if letters.lower() in vowels:  
        count += 1

print(count)