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

def insertion_sort(inputList): 
    count = 0
    for element_index in range(1, len(inputList)): 
        currentValue = inputList[element_index] 
        position = element_index - 1 
        while position >= 0 and currentValue < inputList[position]: 
            count += 1
            inputList[position + 1] = inputList[position] 
            position -= 1 
        inputList[position + 1] = currentValue 
    return inputList, count

def main():
    myList = [1, 5, 7, 9, 4, 2, 3, 6, 10, 8] 
    sortedList = insertion_sort(myList) 
    print(sortedList) 
    print(count)

if __name__ == "__main__":
    main()
