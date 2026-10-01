"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
import time

def generateSortedList(size, minVal=1, maxVal=1000):
    return sorted([random.randint(minVal, maxVal) for _ in range(size)])

def binarySearchIterative(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

def binarySearchRecursive(arr, target, low, high):
    if low > high:
        return -1
        
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearchRecursive(arr, target, mid + 1, high)
    else:
        return binarySearchRecursive(arr, target, low, mid - 1)

def benchmark(sizes):
    print(f"\n{'Size':<10} | {'Iterative (s)':<15} | {'Recursive (s)':<15}")
    print("-" * 46)
    
    for size in sizes:
        testData = generateSortedList(size)
        target = random.choice(testData)
        
        startTime = time.perf_counter()
        binarySearchIterative(testData, target)
        iterTime = time.perf_counter() - startTime
        
        startTime = time.perf_counter()
        binarySearchRecursive(testData, target, 0, len(testData) - 1)
        recTime = time.perf_counter() - startTime
        
        print(f"{size:<10} | {iterTime:<15.8f} | {recTime:<15.8f}")

def main():
    sampleList = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    targetVal = 23
    
    iterIndex = binarySearchIterative(sampleList, targetVal)
    recIndex = binarySearchRecursive(sampleList, targetVal, 0, len(sampleList) - 1)
    
    print("Sorted List:     ", sampleList)
    print("Target Value:    ", targetVal)
    print("Iterative Index: ", iterIndex)
    print("Recursive Index: ", recIndex)
    
    testSizes = [100, 1000, 10000, 100000]
    benchmark(testSizes)

if __name__ == "__main__":
    main()
