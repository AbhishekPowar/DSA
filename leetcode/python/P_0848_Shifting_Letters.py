from typing import List


class Solution:

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = []
        N = len(s)
        curShift = 0

        for idx in range(N):
            # without extra variable
            # curShift += shifts[N-1-idx]
            # newChar = chr(((ord(s[N-1-idx])-97+curShift) % 26)+97)

            curShift = (curShift + shifts[N-1-idx]) % 26
            alphabetIndex = ord(s[N-1-idx]) - 97
            alphabetIndexAfterShift = (alphabetIndex + curShift) % 26
            newChar = chr(alphabetIndexAfterShift+97)
            result.append(newChar)

        result.reverse()
        return ''.join(result)

    def shiftingLettersTwoLoops(self, s: str, shifts: List[int]) -> str:
        result = []
        cummulativeShifts = []
        curSum = 0
        for shift in shifts[::-1]:
            curSum += shift
            cummulativeShifts.append(curSum)
        cummulativeShifts.reverse()

        for idx, shift in enumerate(cummulativeShifts):
            newChar = chr(((ord(s[idx])-97+shift) % 26)+97)
            result.append(newChar)

        return ''.join(result)


if __name__ == "__main__":
    s = 'abc'
    shifts = [3, 5, 9]
    output = Solution().shiftingLetters(s, shifts)
    print(output)
