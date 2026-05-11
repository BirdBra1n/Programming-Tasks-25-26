"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def find_min_max(values):
    maxNum = values[0]
    minNum = values[0]
    if values == [""]:
        return 0
    else:
        for num in values:
            if num > maxNum:
                maxNum = num
            if num < minNum:
                minNum = num
    return minNum, maxNum

def main():
    values = []
    numList = input("Enter a list of numbers: ")
    values += numList.split(", ")
    print(numList)
    print(find_min_max(values))

if __name__ == "__main__":
    main()
