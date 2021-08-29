from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -(2**31)
        curSum = 0
        for n in nums:
            curSum += n
            maximum = max(maximum, curSum)
            if curSum < 0:
                curSum = 0

        return maximum


if __name__ == "__main__":
    nums = [-100, -2, -3]
    output = Solution().maxSubArray(nums)
    print(output)
