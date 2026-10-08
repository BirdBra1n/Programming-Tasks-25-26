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

def main():
    myList = [10, 8, 9, 6, 7, 5, 6, 3, 2, 1]
    sortedList, totalSwaps = bubbleSort(myList)
    
    print("Original List:", myList)
    print("Sorted List:  ", sortedList)
    print("Swaps:        ", totalSwaps)

def bubble(list):
    length = len(list)
    for i in range(length - 1):
        for j in range(0, length - 1):
            if list[j] > list[j+i]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def main():
    list = [10, 8, 9, 6, 7, 5, 6, 3, 2, 1]
    print(bubble(list))

if __name__ == "__main__":
    main()
