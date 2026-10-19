# number = 16
# for a in range (1, number+1):
#     for b in range(1, number+1):
#         print(a*b, end=" ")
#     print()

# width = 6
# length = 4
# for a in range (1, length+1):
#     if a == 1 or a == length:
#         for b in range(1, width+1):
#             print('*', end=" ")
#     else:
#         for b in range(1, width+1):
#             if b == 1 or b == width:
#                 print('*', end=" ")
#             else:
#                 print("#", end=" ")
    
#     print()

width = 6
for i in range(1, width+1):
    print("*"*i, end="\n")