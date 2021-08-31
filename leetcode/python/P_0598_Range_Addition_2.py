# Explains logic
# https://www.youtube.com/watch?v=68VmQaocWkQ&ab_channel=CodingDecoded
from typing import List


class Solution:
    def maxCountBrute(self, m: int, n: int, ops: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for x, y in ops:
            for r in range(x):
                for c in range(y):
                    matrix[r][c] += 1

        [print(row) for row in matrix]
        countHashMap = {}
        for row in matrix:
            for element in row:
                countHashMap[element] = countHashMap.get(element, 0)+1

        return countHashMap[max(countHashMap)]

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # find minimum of x and minimum y in ops that sub matrix is going to be updated most number of times
        if ops:
            for x, y in ops:
                m = min(m, x)
                n = min(n, y)
        return m*n


if __name__ == "__main__":
    m = 3
    n = 3
    ops = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3],
           [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
    output = Solution().maxCount(m, n, ops)
    print(output)
