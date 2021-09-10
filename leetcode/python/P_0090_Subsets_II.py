from typing import List


class Solution:
    def subsetsWithDupRecursive(self, nums):
        self.allSubsets = set()
        nums.sort()
        self.calcSubset(nums, 0, len(nums), [])
        return self.allSubsets

    def calcSubset(self, nums,  idx, lenOfNums, temp):
        if idx < lenOfNums:
            self.calcSubset(nums, idx+1, lenOfNums, temp[:])
            temp.append(nums[idx])
            self.calcSubset(nums, idx+1, lenOfNums, temp[:])
        else:
            self.allSubsets.add(tuple(temp))

    def subsetsWithDupBitMap(self, nums):
        allSubsets = set()
        nums.sort()
        N = len(nums)
        for n in range(2**N):
            binaryRepr = bin(n)[2:]
            subset = []
            for idx, bit in enumerate(binaryRepr[::-1]):
                if bit == '1':
                    subset.append(nums[idx])
            allSubsets.add(tuple(subset))
        return allSubsets

    def subsetsWithDup(self, nums):
        self.allSubsets = []
        self.backtractHelper(nums, 0, len(nums), [])
        return self.allSubsets

    def backtractHelper(self, nums, idx, lenOfNums, temp):
        self.allSubsets.append(temp[:])
        if idx < lenOfNums:
            for i in range(idx, lenOfNums):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                self.backtractHelper(nums, i+1, lenOfNums, temp)
                temp.pop()


if __name__ == "__main__":
    # [[],[1],[1,2],[1,2,2],[2],[2,2]]
    nums = [1, 2, 2, 2, 2]
    output = Solution().subsetsWithDup(nums)
    print(output)
