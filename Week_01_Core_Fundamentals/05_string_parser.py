"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

sentence = input("Enter a sentence: ")

words = []
currentWord = ""

for char in sentence:
    if char == " ":
        words.append(currentWord)
        currentWord = ""
    else:
        currentWord = currentWord + char
words.append(currentWord)

def main():
    print("Number of words:", len(words))
    print("List of words:", words)
    
if __name__ == "__main__":
    main()
