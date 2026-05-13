"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def reverse_list_inplace(values):
    n = len(values)
    for i in range(n // 2):
        temp = values[i]
        values[i] = values[n - 1 - i]
        values[n - 1 - i] = temp
    return values

def main():
    random_integers = [random.randint(1, 100) for _ in range(8)]
    print(random_integers)
    reversed_data = reverse_list_inplace(random_integers)
    print(reversed_data)

if __name__ == "__main__":
    main()
