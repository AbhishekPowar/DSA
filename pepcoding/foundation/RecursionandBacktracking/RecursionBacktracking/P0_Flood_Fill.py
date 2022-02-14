class Solution():

    def floodFill(self, maze, sr, sc, path):

        # @staticmethod
        def floodFillImpl(maze, r, c, path):
            if r == sr-1 and c == sc - 1:
                answers.append(path)
            else:
                directions = ((0, -1, 't'), (-1, 0, 'l'),
                              (0, 1, 'd'), (1, 0, 'r'))
                isVisited[r][c] = 1
                for x, y, ch in directions:
                    nr, nc = ((r+y), (c+x))
                    if 0 <= nr < sr and 0 <= nc < sc and maze[nr][nc] == 0 and isVisited[nr][nc] == 0:
                        print('hit',nr,nc)
                        floodFillImpl(maze, nr, nc, path +
                                      ch, )
                isVisited[r][c] = 1
        isVisited = [[0 for i in range(sc)] for x in range(sr)]
        answers = []
        floodFillImpl(maze, 0, 0, '')
        return answers


if __name__ == "__main__":
    rows,columns = [int(x) for x in input().strip().split(' ')]
    maze = [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    maze = [[int(i) for i in input().strip().split(' ')] for _ in range(rows)]
    sr = len(maze)
    sc = len(maze[0])
    print(maze,sr,sc)
    output = Solution().floodFill(maze, sr, sc, '')
    [print(out) for out in output]
