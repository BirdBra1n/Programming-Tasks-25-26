"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def print_times_table(number):
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def get_valid_integer():
    while True:
        user_input = input("Enter an integer to see its times table: ")
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input, enter a whole number.")

def main():
    target_number = get_valid_integer()
    print_times_table(target_number)

if __name__ == "__main__":
    main()
