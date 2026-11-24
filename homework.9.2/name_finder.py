from sys import argv

def usage():
    print("python3 name_finder.py [name] [year]")

file_year = open(f"babynames-main\\data\\yob{argv[2]}.txt", "r")
rank = 0
argv[1] = argv[1].capitalize()
amount = 10^5
while True:
    line = file_year.readline()
    if line == "":
        print(f"Fewer than 5 children were named {argv[1]} in {argv[2]}")
        break
    else:
        line = line.split(",")

    if amount != int(line[1].replace("\n","")):
        rank +=1
        amount = int(line[1].replace("\n",""))
    if line[0] == argv[1]:
        print(f"{argv[1]}'s rank in {argv[2]} = {rank}")
        break