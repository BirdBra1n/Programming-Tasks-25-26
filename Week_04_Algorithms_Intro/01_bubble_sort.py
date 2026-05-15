"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def bubble(list):
    length = len(list)
    for i in range(length - 1):
        for j in range(0, length - 1):
            if list[j] > list[j+i]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def main():
    list = [10, 8, 9, 6, 7, 5, 6, 3, 2, 1]
    print(bubble(list))

if __name__ == "__main__":
    main()
