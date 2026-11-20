from sys import argv
def int_usage()->None:
    """Prints a usage error to the screen and then ends the program
    """
    print("Usage: cli.py [name] [number]<-!! \n [numer] must be an integer greater than 0")
    exit()

if len(argv) > 2:
    try:
        argv[2] = int(argv[2])
    except ValueError:
        int_usage()
    
    if argv[2] <= 0:
        int_usage()
    print((argv[1]+"\n")*argv[2])
else:
    print("Usage: cli.py [name]<-!! [number]<-!! \n please input a string [name] and a integer [number]")

#1. What is printed? the contents of argv
#2. What data type is argv? a list of strings

