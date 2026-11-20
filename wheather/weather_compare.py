from sys import argv

def usage():
    print("weather_compare.py [RAIN/HOT/COLD/WIND]")

catigory = argv[1].upper()
if catigory == "RAIN":
    sort = 1
elif catigory == "HOT":
    sort = 2
elif catigory == "COLD":
    sort = 3
elif catigory == "WIND":
    sort = 4
else:
    usage()
    exit()

file = open("kleb-weather-2023.csv", "r")
line = file.readline()
most = file.readline()
line = most
while line != "":
    data = line.split(",")
    data[sort] = data[sort].replace("\n", '')
    print(data)
    if float(data[sort]) > float(most[sort]) and sort != 3:
        most = data
    elif sort == 3 and float(data[sort]) < float(most[sort]):
        most = data
    line = file.readline()

print(most)
file.close()
exit()