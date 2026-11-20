file = open("contain_zip\\filename.txt", 'w')
file.write("That's right, I'm Sokka,\n")
file.write("It's pronounced with an 'okka',\n")
file.write("Young ladies, I rocked ya!\n")
file.close()

file = open("contain_zip\\filename.txt", 'r')
lines = file.readlines()
for i in lines:
    print(i)
file.close()