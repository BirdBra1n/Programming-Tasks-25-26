"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
import time

def insertionSort(inputList):
    arr = list(inputList)
    comparisons = 0
    
    for elementIndex in range(1, len(arr)):
        currentValue = arr[elementIndex]
        position = elementIndex - 1
        
        while position >= 0:
            comparisons += 1
            if arr[position] > currentValue:
                arr[position + 1] = arr[position]
                position -= 1
            else:
                break
                
        arr[position + 1] = currentValue
        
    return arr, comparisons

def generateRandomList(size):
    return [random.randint(1, 100) for _ in range(size)]

def benchmark(sizes):
    print(f"\n{'Size':<10} | {'Comparisons':<15} | {'Time (s)':<12}")
    print("-" * 42)
    
    for size in sizes:
        testData = generateRandomList(size)
        
        startTime = time.perf_counter()
        _, totalComps = insertionSort(testData)
        endTime = time.perf_counter()
        
        elapsedTime = endTime - startTime
        print(f"{size:<10} | {totalComps:<15} | {elapsedTime:<12.6f}")

def main():
    myList = [1, 5, 7, 9, 4, 2, 3, 6, 10, 8]
    sortedList, comps = insertionSort(myList)
    
    print("Original List:", myList)
    print("Sorted List:  ", sortedList)
    print("Comparisons:  ", comps)
    
    testSizes = [10, 100, 500, 1000]
    benchmark(testSizes)

if __name__ == "__main__":
    main()
    main()
