RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m' 

#What is this for?
for i in range(2):
    if i == 0: print(f"{'\033[m'}Hello, World!{RESET}")
    elif i == 1: print(f"{BLUE}Goodbye!{RESET}")
    
# print("pick a color:")
# color = input()
# print(f"{color}Hello, World!{RESET}")