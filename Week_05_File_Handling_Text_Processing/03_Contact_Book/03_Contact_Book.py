"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def addContact(fileName, contactName, phoneNumber, emailAddress):
    formattedRecord = contactName + "," + phoneNumber + "," + emailAddress + "\n"
    file = open(fileName, "a")
    file.write(formattedRecord)
    file.close()
    print("Contact saved")


def displayAllContacts(fileName):
    try:
        file = open(fileName, "r")
        fileLines = file.readlines()
        file.close()

        if len(fileLines) == 0:
            print("The contact book is empty.")
        else:
            print("\n--- Complete contact list ---")
            for line in fileLines:
                contactData = line.strip().split(",")
                if len(contactData) == 3:
                    print("Name: " + contactData[0] + " | Phone: " + contactData[1] + " | Email: " + contactData[2])
    except FileNotFoundError:
        print("No contacts found. Add a contact to create the database file.")


def searchContact(fileName, searchTarget):
    try:
        file = open(fileName, "r")
        fileLines = file.readlines()
        file.close()

        targetRecordFound = False
        normalizedTarget = searchTarget.lower()

        print("\n--- Sequential Search Results ---")
        for line in fileLines:
            contactData = line.strip().split(",")
            if len(contactData) == 3:
                if normalizedTarget in contactData[0].lower():
                    print("Found Name: " + contactData[0] + " | Phone: " + contactData[1] + " | Email: " + contactData[2])
                    targetRecordFound = True

        if not targetRecordFound:
            print("Contact Not found")
    except FileNotFoundError:
        print("The contact file does not exist")


def main():
    databaseFileName = "contacts.txt"
    userChoice = ""

    while userChoice != "4":
        print("\n--- Contact book menu ---")
        print("1. Add new contact")
        print("2. Search contacts")
        print("3. Display all contacts")
        print("4. Exit application")

        userChoice = input("Select an option (1-4): ")

        if userChoice == "1":
            nameInput = input("Enter contact name: ")
            phoneInput = input("Enter phone number: ")
            emailInput = input("Enter email address: ")
            addContact(databaseFileName, nameInput, phoneInput, emailInput)
        elif userChoice == "2":
            queryInput = input("Enter name search target: ")
            searchContact(databaseFileName, queryInput)
        elif userChoice == "3":
            displayAllContacts(databaseFileName)
        elif userChoice == "4":
            print("Exiting")
        else:
            print("Invalid input. Please choose options 1-4")


if __name__ == "__main__":
    main()
