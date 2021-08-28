class Solution():

    def floodFill(self, maze, sr, sc, path):

        # @staticmethod
        def floodFillImpl(maze, r, c, path, visited):
            if r == sr-1 and c == sc - 1:
                answers.append(path)
            else:
                directions = ((0, -1, 't'), (-1, 0, 'l'),
                              (0, 1, 'd'), (1, 0, 'r'))
                visited.add((r, c))
                for x, y, ch in directions:
                    nr, nc = ((r+y), (c+x))
                    if 0 <= nr < sr and 0 <= nc < sc and maze[nr][nc] == 0:
                        if (nr, nc) not in visited:
                            floodFillImpl(maze, nr, nc, path +
                                          ch, visited.copy())
        answers = []
        floodFillImpl(maze, 0, 0, '', set())
        return answers


if __name__ == "__main__":
    # rows,columns = [int(x) for x in input().split(' ')]
    maze = [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    # maze = [[int(x) for i in input().split(' ')] for x in range(rows)]
    sr = len(maze)
    sc = len(maze[0])
    output = Solution().floodFill(maze, sr, sc, '')
    [print(out) for out in output]
