"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import os
import matplotlib.pyplot as plt

fileName = "meantemp_daily_totals.txt"


def readTemperatureData(filePath=fileName):
    dateList = []
    tempList = []

    if not os.path.exists(filePath):
        print(f"Error: File '{filePath}' not found.")
        print("Please download 'meantemp_daily_totals.txt' from:")
        print("https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html")
        return dateList, tempList

    dataFile = open(filePath, mode="r", encoding="utf-8")
    
    for line in dataFile:
        parts = line.strip().split()

        if len(parts) < 2 or not parts[0].replace("-", "").isdigit():
            continue

        try:
            if len(parts) >= 2 and "-" in parts[0]:
                dateStr = parts[0]
                tempVal = float(parts[1])
            elif len(parts) >= 4:
                dateStr = f"{parts[0]}-{parts[1].zfill(2)}-{parts[2].zfill(2)}"
                tempVal = float(parts[3])
            else:
                continue

            if tempVal > -50.0:
                dateList.append(dateStr)
                tempList.append(tempVal)

        except ValueError:
            continue

    dataFile.close()
    return dateList, tempList


def calculateStatistics(tempList):
    if len(tempList) == 0:
        print("No valid temperature data found.")
        return None, None, None
    highestTemp = max(tempList)
    lowestTemp = min(tempList)
    averageTemp = sum(tempList) / len(tempList)
    return highestTemp, lowestTemp, averageTemp

def printStatistics(highestTemp, lowestTemp, averageTemp, totalRecords):
    print("--- MET office daily temp stats ---")
    print(f"Total Records Analyzed : {totalRecords}")
    print(f"Highest Temperature    : {highestTemp:.2f} °C")
    print(f"Lowest Temperature     : {lowestTemp:.2f} °C")
    print(f"Average Temperature    : {averageTemp:.2f} °C")

def plotDailyTemperatures(dateList, tempList):
    if len(tempList) == 0:
        print("Cannot plot graph: No data available.")
        return

    plt.figure(figsize=(12, 6))
    plt.plot(tempList, color="tab:blue", linewidth=0.5, label="Daily Mean Temp (°C)")
    
    plt.title("Central England Daily Mean Temperature Over Time", fontsize=14)
    plt.xlabel("Days (from start of dataset)", fontsize=11)
    plt.ylabel("Temperature (°C)", fontsize=11)
    plt.axhline(0, color="red", linestyle="--", linewidth=0.8, label="0°C Freezing Line")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    
    plt.show()


def main():
    dateList, tempList = readTemperatureData(fileName)

    if len(tempList) > 0:
        highestTemp, lowestTemp, averageTemp = calculateStatistics(tempList)
        printStatistics(highestTemp, lowestTemp, averageTemp, len(tempList))

        plotChoice = input("\nWould you like to generate a plot using Matplotlib? (y/n): ").lower()
        if plotChoice == "y":
            plotDailyTemperatures(dateList, tempList)


if __name__ == "__main__":
    main()
