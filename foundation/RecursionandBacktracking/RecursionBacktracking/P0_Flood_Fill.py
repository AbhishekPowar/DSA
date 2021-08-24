class Solution():

    def floodFill(self, image, sr, sc, newColor):
        def floodFillImpl(image, sr, sc, newColor, oldColour, M, N):
            seen.add((sr, sc))
            if 0 <= sr < M and 0 <= sc < N and image[sr][sc] == oldColour:
                image[sr][sc] = newColor
                for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    if ((sr+x), (sc+y)) not in seen:
                        floodFillImpl(image, sr+x, sc+y,
                                      newColor, oldColour, M, N)
        M = len(image)
        N = len(image[0])
        seen = set()
        oldColour = image[sr][sc]
        floodFillImpl(image, sr, sc, newColor, oldColour, M, N)
        return image


if __name__ == "__main__":
    image = [
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1]]
    image = [
            [0, 0, 0],
            [0, 0, 0]
    ]
    sr = 0
    sc = 0
    newColor = 2
    outputImage = Solution().floodFill(image, sr, sc, newColor)
    [print(x) for x in outputImage]
