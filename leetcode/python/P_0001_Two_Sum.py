class Solution:
    def twoSum(self, nums, target):
        seenArr = dict()
        for idx, num in enumerate(nums):
            if target-num in seenArr:
                return [seenArr[target-num], idx]
            else:
                seenArr[num] = idx
        return [-1, -1]


def main():
    ar = [1, 2, 3, 4, 5, 7, 9]
    target = 9
    output = Solution().twoSum(ar, target)
    print(output)


if __name__ == "__main__":
    main()
