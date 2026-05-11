def calculate_average(values):
    sumNums = 0
    count = 0
    if values == [""]:
        return 0
    else:
        for num in values:
            sumNums += int(num.strip())
            count += 1
        return sumNums / count
    
values = []
numList = input("Enter a list of numbers: ")
values += numList.split(",")
print(numList)
print(calculate_average(values))
