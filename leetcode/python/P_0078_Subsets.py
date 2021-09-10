from typing import List


class Solution:
    def subsetsRecursive(self, nums: List[int]) -> List[List[int]]:
        def calcSubset(nums,  idx, lenOfNums, temp):
            if idx < lenOfNums:
                calcSubset(nums, idx+1, lenOfNums, temp[:])
                temp.append(nums[idx])
                calcSubset(nums, idx+1, lenOfNums, temp[:])
            else:
                self.allSubsets.append(temp)
        self.allSubsets = []
        calcSubset(nums, 0, len(nums), [])
        return self.allSubsets

    def subsetsBitMap(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        N = len(nums)
        for n in range(2**N):
            binaryRepr = bin(n)[2:]
            subset = []
            for idx, bit in enumerate(binaryRepr[::-1]):
                if bit == '1':
                    subset.append(nums[idx])
            allSubsets.append(subset)
        return allSubsets

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtractHelper(nums, idx, lenOfNums, temp):
            self.allSubsets.append(temp[:])
            if idx < lenOfNums:
                for i in range(idx, lenOfNums):
                    temp.append(nums[i])
                    backtractHelper(nums, i+1, lenOfNums, temp)
                    temp.pop()
        self.allSubsets = []
        backtractHelper(nums, 0, len(nums), [])
        return self.allSubsets

    def subsetsBfs(self, nums):
        allSubsets = [[]]
        for i in nums:
            size = len(allSubsets)
            for subIdx in range(size):
                newSubset = allSubsets[subIdx]+[i]
                allSubsets.append(newSubset)
        return allSubsets


if __name__ == "__main__":
    nums = [1, 2, 3]
    # output = Solution().subsets(nums)
    output = Solution().subsetsRecursive(nums)
    print(output)
