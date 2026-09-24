#Task
from typing import List

def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    
    for i in zero_rows:
        for j in range(cols):
            matrix[i][j] = 0

    
    for j in zero_cols:
        for i in range(rows):
            matrix[i][j] = 0

    return matrix


if __name__ == '__main__':
    matrix = []
    while True:
        line = input()
        if not line.strip():
            break
        row = list(map(int, line.split()))
        matrix.append(row)

    print(setZeroes(matrix))