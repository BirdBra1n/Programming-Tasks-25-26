"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


def analyzeFile(fileName):
    try:
        file = open(fileName, "r")
        fileLines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: File not found")
        return 0, 0, 0, ""

    lineCount = len(fileLines)
    wordCount = 0
    charCount = 0
    wordFrequencies = {}

    for line in fileLines:
        charCount = charCount + len(line)

        cleanedLine = ""
        for char in line:
            if char.isalnum() or char.isspace():
                cleanedLine = cleanedLine + char.lower()
            else:
                cleanedLine = cleanedLine + " "

        lineWords = cleanedLine.split()
        wordCount = wordCount + len(lineWords)

        for currentWord in lineWords:
            if currentWord in wordFrequencies:
                wordFrequencies[currentWord] = wordFrequencies[currentWord] + 1
            else:
                wordFrequencies[currentWord] = 1

    mostFrequentWord = ""
    highestFrequency = 0

    for word in wordFrequencies:
        if wordFrequencies[word] > highestFrequency:
            highestFrequency = wordFrequencies[word]
            mostFrequentWord = word

    return lineCount, wordCount, charCount, mostFrequentWord


def main():
    FileName = "sampleTest.txt"

    lineResults, wordResults, charResults, freqResult = analyzeFile(FileName)

    if lineResults > 0:
        print("Number of lines:      ", lineResults)
        print("Number of words:      ", wordResults)
        print("Number of characters: ", charResults)
        print("Most frequent word:   '" + freqResult + "'")


if __name__ == "__main__":
    main()
