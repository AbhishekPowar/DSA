
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {'M': 1000, 'D': 500, 'C': 100,
                      'L': 50, 'X': 10, 'V': 5, 'I': 1}
        output = 0
        lenOfString = len(s)-1
        for index, char in enumerate(s):
            if index == lenOfString or romanToInt[s[index]] >= romanToInt[s[index+1]]:
                output += romanToInt[s[index]]
            else:
                output -= romanToInt[s[index]]
        return output


if __name__ == "__main__":
    s = 'MCMXCIV'
    output = Solution().romanToInt(s)
    print(output)
