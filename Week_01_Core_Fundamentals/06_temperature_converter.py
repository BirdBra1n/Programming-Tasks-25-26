"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Quit")
        
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            try:
                c = float(input("Enter temperature in Celsius: "))
                f = celsius_to_fahrenheit(c)
                print(f"{c}°C is equal to {f}°F")
            except ValueError:
                print("Enter a valid number!")

        elif choice == "2":
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                c = fahrenheit_to_celsius(f)
                print(f"{f}°F is equal to {c}°C")
            except ValueError:
                print("Enter a valid number!")

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
