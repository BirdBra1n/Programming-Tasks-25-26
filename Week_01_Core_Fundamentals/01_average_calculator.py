"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def calculate_average(values):
    sumNums = 0
    count = 0
    if values == [""]:
        return 0
    else:
        for num in values:
            sumNums += int(num.strip())
            count += 1
        return sumNums / count

def main():
values = []
numList = input("Enter a list of numbers: ")
values += numList.split(",")
print(numList)
print(calculate_average(values))

if __name__ == "__main__":
    main()
