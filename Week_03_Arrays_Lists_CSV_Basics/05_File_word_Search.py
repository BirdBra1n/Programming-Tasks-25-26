"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import os

def countLinesWithTerm(fileName, searchTerm, caseSensitive=False):
    if not os.path.exists(fileName):
        print(f"\nError: File '{fileName}' not found.")
        return 0, 0

    matchingLineCount = 0
    totalLineCount = 0

    fileHandle = open(fileName, mode="r", encoding="utf-8", errors="ignore")

    for lineText in fileHandle:
        totalLineCount = totalLineCount + 1
        
        currentLine = lineText if caseSensitive else lineText.lower()
        targetTerm = searchTerm if caseSensitive else searchTerm.lower()

        if targetTerm in currentLine:
            matchingLineCount = matchingLineCount + 1

    fileHandle.close()
    return matchingLineCount, totalLineCount


def searchAndDisplayMatches(fileName, searchTerm, caseSensitive=False):
    if not os.path.exists(fileName):
        print(f"\nError: File '{fileName}' not found.")
        return
    
    fileHandle = open(fileName, mode="r", encoding="utf-8", errors="ignore")
    lineNumber = 0
    matchFound = False

    for lineText in fileHandle:
        lineNumber = lineNumber + 1
        
        currentLine = lineText if caseSensitive else lineText.lower()
        targetTerm = searchTerm if caseSensitive else searchTerm.lower()

        if targetTerm in currentLine:
            cleanLine = lineText.strip()
            print(f"Line {lineNumber:<6}: {cleanLine[:80]}")
            matchFound = True

    fileHandle.close()

    if not matchFound:
        print("No matching lines found.")


def main():
    print("--- File word search tool ---")

    fileName = input("Enter the filename to search (e.g. sherlock.txt): ").strip()
    searchTerm = input("Enter the search term/word: ").strip()

    caseChoice = input("Case-sensitive search? (y/n): ").strip().lower()
    isCaseSensitive = (caseChoice == "y")

    matchingLines, totalLines = countLinesWithTerm(fileName, searchTerm, isCaseSensitive)

    if totalLines > 0:
        print("\n--- Results ---")
        print(f"Total lines scanned : {totalLines}")
        print(f"Matching lines      : {matchingLines}")
        
        if totalLines > 0:
            percentage = (matchingLines / totalLines) * 100
            print(f"Percentage of lines : {percentage:.2f}%")
            
        previewChoice = input("\nWould you like to preview matching lines? (y/n): ").strip().lower()
        if previewChoice == "y":
            searchAndDisplayMatches(fileName, searchTerm, isCaseSensitive)

if __name__ == "__main__":
    main()
    
