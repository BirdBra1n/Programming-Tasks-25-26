"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def linear_search(values, target):
    index = 0
    found = False
    position = -1

    while index < len(values) and not found:
        if values[index] == target:
            found = True
            position = index
        else:
            index = index + 1
    return position

def main():
    testArray = [24, 17, 85, 63, 91, 12]
    searchTarget = 63
    
    result = linear_search(testArray, searchTarget)
    print(result)
    
if __name__ == "__main__":
    main()
