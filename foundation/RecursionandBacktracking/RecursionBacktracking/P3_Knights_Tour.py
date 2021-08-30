class Solution:
    def knightsTour(self, n, row, column):
        def isValid(r, c, n):
            return 0 <= r < n and 0 <= c < n and visited[r][c] == -1

        def knightProbabilityImpl(n,  row, column, cur):
            visited[row][column] = cur
            if cur == 25:
                self.count += 1
                if self.count > 1:
                    print()
                for i in visited:
                    for j in i:
                        print(j, end=' ')
                    print()
            for x, y in ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)):
                if isValid(row+x, column+y, n):
                    knightProbabilityImpl(n, row+x, column+y, cur+1)
            visited[row][column] = -1
        visited = [[-1 for _ in range(n)] for _ in range(n)]
        self.count = 0
        knightProbabilityImpl(n, row, column, cur=1)


if __name__ == "__main__":
    n, row, column = 5, 2, 0
    Solution().knightsTour(n, row, column)
