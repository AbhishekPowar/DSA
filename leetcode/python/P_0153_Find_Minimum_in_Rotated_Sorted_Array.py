from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarySearchMod(nums, low, high):
            print(low, high)
            if low < high:
                mid = (low+high) // 2
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                elif nums[mid] < last:
                    return binarySearchMod(nums, low, mid-1)
                else:
                    return binarySearchMod(nums, mid+1, high)
            else:
                return nums[low]

        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        last = nums[-1]
        return binarySearchMod(nums, 0, len(nums)-1)


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    output = Solution().findMin(nums)
    print(output)
