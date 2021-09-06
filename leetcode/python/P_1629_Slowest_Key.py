from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        N = len(keysPressed)
        maxDuration = releaseTimes[0]
        maxChar = keysPressed[0]
        for idx in range(1, N):
            curMax = releaseTimes[idx]-releaseTimes[idx-1]
            curChar = keysPressed[idx]
            if curMax == maxDuration and curChar < maxChar:
                continue
            if curMax >= maxDuration:
                maxDuration = curMax
                maxChar = curChar

        return maxChar


if __name__ == "__main__":
    releaseTimes = [12, 23, 36, 46, 62]
    keysPressed = "spuda"
    output = Solution().slowestKey(releaseTimes, keysPressed)
    print(output)
