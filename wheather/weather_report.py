from sys import argv

def usage():
    print("weather_report.py MM-DD")

try:
    # program to take a dat from the command line and then report the weather
    # from that date

    # parse the input args to get the date
    date = argv[1]

    # then we're going to open the file for reading
    file = open("kleb-weather-2023.csv", "r")

    #then we're going to read the file one line at a time
    line = file.readline()
    while line != "":
        line = file.readline()
    # if we have found the right date, weire going to extract the data, 
        if date in line:
            data = line.split(",")
            precip = float(data[1])
            hightemp = float(data[2])
            lowtemp = float(data[3])
            wind = float(data[4])
            print(f"On {date}-2023, there was {precip}")
            print(f"The high tempeture was {hightemp} and the low was {lowtemp}")
            print(f"the max 5-second wind speed was {wind}")
            file.close()
            exit()

    print("Date not found")
    # then we're going to print out the weather report, stop reading and close the file
except Exception:
    print("something went wrong")
finally:
    file.close()
