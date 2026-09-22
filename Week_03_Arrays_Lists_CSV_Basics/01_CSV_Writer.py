"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import csv

fileName = "user_data.csv"


def appendRecord():
    userName = input("Enter Name: ")
    userAge = input("Enter Age: ")
    favouriteColour = input("Enter Favourite Colour: ")
    extraNote = input("Enter Anything Else: ")
    csvFile = open(fileName, mode="a", newline="")
    csvWriter = csv.writer(csvFile)
    
    csvWriter.writerow([userName, userAge, favouriteColour, extraNote])
    csvFile.close()
    
    print("Record added successfully.")


def readCsv():
    csvFile = open(fileName, mode="r")
    csvReader = csv.reader(csvFile)
    
    fileData = list(csvReader)
    csvFile.close()

    print("\n--- CSV File Contents ---")
    for rowNumber in range(len(fileData)):
        print(rowNumber, fileData[rowNumber])
        
    return fileData


def editRecord():
    fileData = readCsv()
    
    rowToEdit = int(input("\nEnter the row number you want to edit: "))
    
    print(f"Editing row {rowToEdit}: {fileData[rowToEdit]}")
    newUserName = input("Enter New Name: ")
    newUserAge = input("Enter New Age: ")
    newFavouriteColour = input("Enter New Favourite Colour: ")
    newExtraNote = input("Enter New Anything Else: ")

    fileData[rowToEdit] = [newUserName, newUserAge, newFavouriteColour, newExtraNote]

    csvFile = open(fileName, mode="w", newline="")
    csvWriter = csv.writer(csvFile)
    csvWriter.writerows(fileData)
    csvFile.close()
    
    print("Record updated successfully.")


def main():
    userChoice = ""
    
    while userChoice != "4":
        print("\n--- Menu ---")
        print("1. Read File")
        print("2. Append Record")
        print("3. Edit Record")
        print("4. Exit")
        
        userChoice = input("Choose an option (1-4): ")

        if userChoice == "1":
            readCsv()
        elif userChoice == "2":
            appendRecord()
        elif userChoice == "3":
            editRecord()
        elif userChoice == "4":
            print("Goodbye!")


if __name__ == "__main__":
    main()
