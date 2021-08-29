from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        def hashMapWay(nums):
            numsSet = set(nums)
            return len(nums) != len(numsSet)

        def sortingWay(nums):
            nums.sort()
            for idx in range(1, len(nums)):
                if nums[idx] == nums[idx-1]:
                    return True
            return False

        return sortingWay(nums)


if __name__ == "__main__":
    nums = [1, 1]
    output = Solution().containsDuplicate(nums)
    print(output)
