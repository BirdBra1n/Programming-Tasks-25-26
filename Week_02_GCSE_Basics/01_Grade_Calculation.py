"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "D"

def main():
    try:
        user_input = input("Enter your percentage grade (0-100): ")
        score = int(user_input)
        
        if 0 <= score <= 100:
            letter_grade = get_grade(score)
            print(f"A score of {score}% is equivalent of the grade of: {letter_grade}")
        else:
            print("Invalid input, enter a score between 0 and 100.")
            
    except ValueError:
        print("Invalid input, Please enter a numerical value.")


if __name__ == "__main__":
    main()
