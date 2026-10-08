"""
TASK: 02 Simple Logger System

# Create a script that appends time-stamped log entries to a file.
Menu:
- Add Log
- View Log
- Clear Log

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


import datetime

def addLogEntry(fileName, logMessage):
    currentTime = datetime.datetime.now()
    timeStamp = currentTime.strftime("%Y-%m-%d %H:%M:%S")
    formattedEntry = "[" + timeStamp + "] " + logMessage + "\n"

    file = open(fileName, "a")
    file.write(formattedEntry)
    file.close()
    print("Log entry added")


def viewLogContents(fileName):
    try:
        file = open(fileName, "r", encoding="utf-8")
        fileContents = file.read()
        file.close()

        if len(fileContents.strip()) == 0:
            print("Log file is empty")
        else:
            print("\n--- Log file contents ---")
            print(fileContents)
            print("-------------------------")
    except FileNotFoundError:
        print("Log file does not exist")


def clearLogFile(fileName):
    file = open(fileName, "w")
    file.close()
    print("Log file cleared")


def main():
    logFileName = "logFile.txt"
    userChoice = ""

    while userChoice != "4":
        print("\n--- Simple logger ---")
        print("1. Add log entry")
        print("2. View log contents")
        print("3. Clear log file")
        print("4. Exit")

        userChoice = input("Select an option (1-4): ")

        if userChoice == "1":
            messageInput = input("Enter log message: ")
            addLogEntry(logFileName, messageInput)
        elif userChoice == "2":
            viewLogContents(logFileName)
        elif userChoice == "3":
            clearLogFile(logFileName)
        elif userChoice == "4":
            print("Exiting")
        else:
            print("Invalid input. Please choose options 1-4")


if __name__ == "__main__":
    main()
