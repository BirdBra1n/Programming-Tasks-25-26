"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
import time

def bubbleSort(inputList):
    arr = list(inputList)
    swaps = 0
    length = len(arr)
    
    for i in range(length - 1):
        swapped = False
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swaps += 1
                swapped = True
        if not swapped:
            break
            
    return arr, swaps

def generateRandomList(size):
    return [random.randint(1, 100) for _ in range(size)]

def benchmark(sizes):
    print(f"\n{'Size':<10} | {'Swaps':<15} | {'Time (s)':<12}")
    print("-" * 42)
    
    for size in sizes:
        testData = generateRandomList(size)
        
        startTime = time.perf_counter()
        _, totalSwaps = bubbleSort(testData)
        endTime = time.perf_counter()
        
        elapsedTime = endTime - startTime
        print(f"{size:<10} | {totalSwaps:<15} | {elapsedTime:<12.6f}")

def main():
    myList = [10, 8, 9, 6, 7, 5, 6, 3, 2, 1]
    sortedList, swaps = bubbleSort(myList)
    
    print("Original List:", myList)
    print("Sorted List:  ", sortedList)
    print("Swaps:        ", swaps)
    
    testSizes = [10, 100, 500, 1000]
    benchmark(testSizes)

if __name__ == "__main__":
    main()
