"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
import matplotlib.pyplot as plt


def simulateRolls(numberOfRolls):
    sideCounts = [0, 0, 0, 0, 0, 0, 0]
    totalSum = 0

    print(f"\n--- Rolling die {numberOfRolls} times ---")
    for rollIndex in range(numberOfRolls):
        rollValue = random.randint(1, 6)
        print(f"Roll {rollIndex + 1}: {rollValue}")
        
        sideCounts[rollValue] = sideCounts[rollValue] + 1
        totalSum = totalSum + rollValue

    return sideCounts, totalSum


def displayStatistics(sideCounts, totalSum, numberOfRolls):
    print("\n--- Dice Stats ---")
    
    for side in range(1, 7):
        sideTotalSum = side * sideCounts[side]
        print(f"Side {side}: count = {sideCounts[side]}, total sum = {sideTotalSum}")

    averageRoll = totalSum / numberOfRolls
    print(f"\nTotal Sum of all rolls: {totalSum}")
    print(f"Average dice roll: {averageRoll:.2f}")


def plotBarGraph(sideCounts):
    sides = [1, 2, 3, 4, 5, 6]
    counts = sideCounts[1:]

    plt.figure(figsize=(8, 5))
    plt.bar(sides, counts, color="skyblue", edgecolor="black")
    plt.title("Dice Roll Frequency Distribution")
    plt.xlabel("Dice Side")
    plt.ylabel("Frequency (Count)")
    plt.xticks(sides)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    plt.show()

def main():
    numberOfRolls = int(input("Enter the number of times to roll the die: "))
    sideCounts, totalSum = simulateRolls(numberOfRolls)
    displayStatistics(sideCounts, totalSum, numberOfRolls)
    
    plotGraphChoice = input("\nWould you like to plot a bar graph? (y/n): ").lower()
    if plotGraphChoice == "y":
        plotBarGraph(sideCounts)

if __name__ == "__main__":
    main()
