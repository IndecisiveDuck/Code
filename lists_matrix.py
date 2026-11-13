#A teacher keeps a gradebook for their class
# a students total grade is determined by N quizes given over the quarter
students = ["Arthur Dent", "Ford Prefect", "Zaphod Beeblebrox", "Trillian"]

grades = [[84, 24, 75, 99, 42],
          [75, 75, 76, 100, 99],
          [65, 80, 90, 100, 67],
          [12, 34, 56, 78, 90]]

# for i in range(len(students)):
#     print(students[i], end=": ")
#     for a in range(len(grades[i])):
#         print(f"quiz {a+1}: {grades[i][a]}", end=", ")
#     print()

lengths = []
for i in range(len(grades)):
    lengths.append(len(grades[i]))

for a in lengths:
    