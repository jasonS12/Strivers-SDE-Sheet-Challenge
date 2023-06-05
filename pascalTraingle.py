from typing import *
def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)

def printPascal(n:int) -> List[List[int]]:
    ans = []

    #Store the entire pascal's triangle:
    for row in range(1, n+1):
        tempLst = [] # temporary list
        for col in range(1, row+1):
            tempLst.append(nCr(row - 1, col - 1))
        ans.append(tempLst)
    return ans
