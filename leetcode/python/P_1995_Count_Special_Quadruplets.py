from typing from List

# scalable solution. Leetcode weekly contest 257
class Solution():
    def solve(self, nums):
        def takeItOrNot(nums, idx, lenOfNums, temp, curSize, last):
            if idx < lenOfNums and curSize < 4:
                takeItOrNot(nums, idx+1, lenOfNums, temp, curSize, last)
                takeItOrNot(nums, idx+1, lenOfNums, temp +
                            nums[idx], curSize+1, nums[idx])
            else:
                if curSize == 4 and last !=-1 and temp == (2 * last):
                    self.output += 1
        self.output = 0
        takeItOrNot(nums, 0, len(nums), 0, 0, last=-1)
        return self.output




if __name__ == "__main__":
    nums = [1, 1, 1, 3, 5]
    output = Solution().solve(nums)
    print(output)
