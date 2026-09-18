s = "Hello, World!"
r = "Idmmp, Xpmse!"
n = 4 

#Can't subtract strings and can't add ints to strings.
mystery = s + r
print(mystery)

a = 42
b = 7

print(a + b)#49 int
print(str(a + b))#does the math then turns it into a string
print(str(a) + str(b))#427 mushes the strings together
name = "Morgen F Putnam"
print(name[-1])
print(name[len(name)//2])

#to get a specific letter of a string do string[number]

new_name = mystery.replace("!", "! ")
print(new_name)