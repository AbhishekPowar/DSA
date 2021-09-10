from typing import List


class Solution:
    def subsetsRecursive(self, nums: List[int]) -> List[List[int]]:
        self.allSubsets = []
        self.calcSubset(nums, 0, len(nums), [])
        return self.allSubsets

    def calcSubset(self, nums,  idx, lenOfNums, temp):
        if idx < lenOfNums:
            self.calcSubset(nums, idx+1, lenOfNums, temp[:])
            temp.append(nums[idx])
            self.calcSubset(nums, idx+1, lenOfNums, temp[:])
        else:
            self.allSubsets.append(temp)

    def subsets(self, nums: List[int]) -> List[List[int]]:
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


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    output = Solution().subsets(nums)
    print(output)
