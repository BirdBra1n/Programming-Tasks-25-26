"""
TASK: 03 Grid Path Counter

# Grid Path Counter - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
Given an NxM grid:
- Count paths using recursion
- Count paths using iteration
Movement allowed: RIGHT or DOWN only.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def countPathsRecursive(n, m):
    if n == 1 or m == 1:
        return 1
    return countPathsRecursive(n - 1, m) + countPathsRecursive(n, m - 1)

def countPathsIterative(n, m):
    dpGrid = [[1] * m for _ in range(n)]
    
    for row in range(1, n):
        for col in range(1, m):
            dpGrid[row][col] = dpGrid[row - 1][col] + dpGrid[row][col - 1]
            
    return dpGrid[n - 1][m - 1]

def main():
    rows = 3
    cols = 3
    
    print("Grid Size:", f"{rows}x{cols}")
    print("Recursive Paths:", countPathsRecursive(rows, cols))
    print("Iterative Paths:", countPathsIterative(rows, cols))

if __name__ == "__main__":
    main()
