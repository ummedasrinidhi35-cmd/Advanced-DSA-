from typing import List
def countNegatives(grid: List[List[int]]) -> int:
    count = 0
    for row in grid:
        for ele in row:
            if ele < 0:
                count += 1
    return count
grid =[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))
#59
from typing import List
def generateMatrix(n: int) -> List[List[int]]:
    top,bottom=0,n-1
    left,right=0,n-1
    res=[[0]*n for _ in range(n)]
    num=1
    while top<=bottom and left<=right:
        #left to right
        for c in range(left,right+1):
            res[top][c]=num
            num+=1
        top+=1 
        #top to bottom
        for r in range(top,bottom+1):
            res[r][right]=num
            num+=1
        right-=1
        if top<=bottom:
            for c in range(right,left-1,-1):
                res[bottom][c]=num
                num+=1
            bottom-=1
        if left<=right:
            for r in range(bottom,top-1,-1):
                res[r][left]=num
                num+=1
            left+=1
    return res
n=3
print(generateMatrix(n))
#867
from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    rows,cols = len(matrix),len(matrix[0])
    res = [[0]*rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            res[c][r] = matrix[r][c]
    return res