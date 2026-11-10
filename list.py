a = ["1","1","2","3","5"]
b = ["8", "13",]

print(a*2) # prints ['1', '1', '2', '3', '5', '1', '1', '2', '3', '5']

print(a+b) # prints ['1', '1', '2', '3', '5', '8', '13']
print(a+list("758"))

c = a
print(a==b) #false
print(a==c) #true

print(a[0]=="1") #true
print(a=="1") #false
print(a==["1","1","2","3","5"]) #true