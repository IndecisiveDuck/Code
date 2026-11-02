#A loop that prints the numbers 1 to 10 in order
for i in range(10):
    print(i+1)

#A loop that prints a countdown from 10 to 1
for i in range(10):
    print(10-i)

#A loop that prints all even numbers from 2 to 20
for i in range(2,21,2):
    print(i)

#A loop that prints all factors of 7 starting at 77 and counting down to 7 
# (so 77, 70, 63, ..., 14, 7)
for i in range(77, 6, -7):
    print(i)

#A loop that prints out a string one letter at a time
string = input("Enter a string: ")
for ch in string:
    print(ch)

#A loop that prints a string backwards
string = input("Enter a string: ")
reversed_text = ""
for ch in string:
    reversed_text = ch + reversed_text
print(reversed_text)

#A loop that prints out every other letter of a string
string = input("Enter a string: ")
for i in range(0, len(string)+1, 2):
    print(string[i])

#for loops use numbers and end when the max number is reached
# for i in range(min, max, iteration):
    #execute code

#while loops execute code while a condition is met
# while condition true:
    #execute code