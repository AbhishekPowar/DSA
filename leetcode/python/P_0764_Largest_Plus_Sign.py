from typing import List


def printmat(mat):
    [print(row) for row in mat]
    print()


class Solution:

    def orderOfLargestPlusSignHighMemory(self, n: int, mines: List[List[int]]) -> int:
        mat = [[1 for _ in range(n)] for _ in range(n)]
        for x, y in mines:
            mat[x][y] -= 1

       # calculate grids
        LTR = [[0 for _ in range(n)] for _ in range(n)]
        RTL = [[0 for _ in range(n)] for _ in range(n)]
        TTB = [[0 for _ in range(n)] for _ in range(n)]
        BTT = [[0 for _ in range(n)] for _ in range(n)]

        cur = 0
        for row in range(n):
            cur = 0
            for col in range(n):
                if mat[row][col] == 1:
                    cur += 1
                else:
                    cur = 0
                LTR[row][col] = cur

        for row in range(n):
            cur = 0
            for col in range(n-1, -1, -1):
                if mat[row][col] == 1:
                    cur += 1
                else:
                    cur = 0
                RTL[row][col] = cur

        for col in range(n):
            cur = 0
            for row in range(n):
                if mat[row][col] == 1:
                    cur += 1
                else:
                    cur = 0
                TTB[row][col] = cur

        for col in range(n):
            cur = 0
            for row in range(n-1, -1, -1):
                if mat[row][col] == 1:
                    cur += 1
                else:
                    cur = 0
                BTT[row][col] = cur

        printmat(LTR)
        printmat(RTL)
        printmat(TTB)
        printmat(BTT)

        largesPlusSize = 0
        for row in range(n):
            for col in range(n):
                howManyOnesInLeft = LTR[row][col]
                howManyOnesInRight = RTL[row][col]
                howManyOnesInTop = TTB[row][col]
                howManyOnesInBottom = BTT[row][col]
                curSizeOfPlus = min(
                    [howManyOnesInBottom, howManyOnesInLeft, howManyOnesInRight, howManyOnesInTop])
                largesPlusSize = max(largesPlusSize, curSizeOfPlus)
        return largesPlusSize

    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mat = [[1 for _ in range(n)] for _ in range(n)]
        for x, y in mines:
            mat[x][y] -= 1

       # calculate grids
        compute = [[0 for _ in range(n)] for _ in range(n)]

        cur = 0
        for row in range(n):
            cur = 0
            for col in range(n):
                if mat[row][col] == 1:
                    cur += 1
                else:
                    cur = 0
                compute[row][col] = cur

        for row in range(n):
            cur = 0
            for col in range(n-1, -1, -1):
                if mat[row][col] == 1:
                    cur += 1
                else:
                    cur = 0
                compute[row][col] = min(compute[row][col], cur)

        for col in range(n):
            cur = 0
            for row in range(n):
                if mat[row][col] == 1:
                    cur += 1
                else:
                    cur = 0
                compute[row][col] = min(compute[row][col], cur)

        for col in range(n):
            cur = 0
            for row in range(n-1, -1, -1):
                if mat[row][col] == 1:
                    cur += 1
                else:
                    cur = 0
                compute[row][col] = min(compute[row][col], cur)

        maxPossible = n//2 if n % 2 == 0 else (n+1)//2
        largesPlusSize = 0
        for row in range(n):
            for col in range(n):
                curSizeOfPlus = compute[row][col]
                largesPlusSize = max(largesPlusSize, curSizeOfPlus)
                if maxPossible == largesPlusSize:
                    return largesPlusSize
        return largesPlusSize


if __name__ == "__main__":
    n = 5
    mines = [[4, 2]]
    output = Solution().orderOfLargestPlusSign(n, mines)
    print(output)
