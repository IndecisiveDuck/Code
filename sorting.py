import time
import random

def selection_sort(a: list[int])-> None:
    # Start with the first element in the list and compare it to all the others
    for i in range(len(a)):
        i_smallest = i
        for j in range(i + 1, len(a)):
            if a[j] < a[i_smallest]:
                i_smallest = j

        # Swap a[i_smallest] and a[i]
        temp = a[i_smallest]
        a[i_smallest] = a[i]
        a[i] = temp

def main():
    list_size = 100000
    numbers = []
    for i in range(list_size):
        numbers.append(random.randint(-10*list_size, 10*list_size))

    tic = time.perf_counter()
    selection_sort(numbers)
    toc = time.perf_counter()
    print(numbers)
    print(toc-tic)

main()