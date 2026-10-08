"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
correctUser = "eddie123"
correctPassword = "password@123"

attemptsRemaining = 3

while attemptsRemaining > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correctUser and password == correctPassword:
        print("\nWelcome")
        break
    else:
        attemptsRemaining -= 1
        if attemptsRemaining > 0:
            print(f"Access denied, {attemptsRemaining} attempts remaining\n")
        else:
            print("Access denied.")

if __name__ == "__main__":
    main()
