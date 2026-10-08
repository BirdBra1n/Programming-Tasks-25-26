"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def printArray(gridData):
    if len(gridData) == 0:
        print("\nThe array is currently empty.")
        return

    print("\n--- Current 2D Array ---")
    for rowIndex in range(len(gridData)):
        rowString = ""
        for colIndex in range(len(gridData[rowIndex])):
            rowString = rowString + f"[{gridData[rowIndex][colIndex]}] "
        print(f"Row {rowIndex}: {rowString}")


def appendValue(gridData):
    print("\n1. Append a new row")
    print("2. Add a value to an existing row")
    userOption = input("Choose option (1-2): ")

    if userOption == "1":
        newRowValue = input("Enter initial value for the new row: ")
        gridData.append([newRowValue])
        print("New row appended successfully.")

    elif userOption == "2":
        if len(gridData) == 0:
            print("Array is empty. Creating Row 0 automatically.")
            newRowValue = input("Enter value for Row 0: ")
            gridData.append([newRowValue])
            return

        targetRow = int(input(f"Enter target row index (0 to {len(gridData) - 1}): "))
        if 0 <= targetRow < len(gridData):
            newValue = input("Enter value to add to this row: ")
            gridData[targetRow].append(newValue)
            print("Value appended to row successfully.")
        else:
            print("Invalid row index.")


def deleteEntry(gridData):
    if len(gridData) == 0:
        print("\n[!] The array is empty. Nothing to delete.")
        return

    printArray(gridData)
    print("\n1. Delete a specific entry by (Row, Column) index")
    print("2. Delete an entire row")
    userOption = input("Choose option (1-2): ")

    if userOption == "1":
        targetRow = int(input("Enter Row index: "))
        if 0 <= targetRow < len(gridData):
            targetCol = int(input("Enter Column index: "))
            if 0 <= targetCol < len(gridData[targetRow]):
                removedValue = gridData[targetRow].pop(targetCol)
                print(f"Removed value '{removedValue}' at [{targetRow}][{targetCol}].")

                if len(gridData[targetRow]) == 0:
                    gridData.pop(targetRow)
                    print(f"Row {targetRow} was empty and has been removed.")
            else:
                print("Invalid column index.")
        else:
            print("Invalid row index.")

    elif userOption == "2":
        targetRow = int(input("Enter Row index to delete: "))
        if 0 <= targetRow < len(gridData):
            deletedRow = gridData.pop(targetRow)
            print(f"Deleted entire row: {deletedRow}")
        else:
            print("Invalid row index.")


def main():
    gridData = [
        ["A1", "A2", "A3"],
        ["B1", "B2"],
        ["C1", "C2", "C3", "C4"]
    ]

    userChoice = ""

    while userChoice != "4":
        print("--- 2D array adder ---")
        print("1. Read all current values")
        print("2. Append new value/row")
        print("3. Delete a chosen entry")
        print("4. Exit")

        userChoice = input("\nSelect an option (1-4): ")

        if userChoice == "1":
            printArray(gridData)
        elif userChoice == "2":
            appendValue(gridData)
        elif userChoice == "3":
            deleteEntry(gridData)
        elif userChoice == "4":
            print("Exiting application. Goodbye!")


if __name__ == "__main__":
    main()
