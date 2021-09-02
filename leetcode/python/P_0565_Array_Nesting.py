from typing import List


class Solution:
    def arrayNestingHashSet(self, nums: List[int]) -> int:
        visted = set()
        maximum = 1
        N = len(nums)
        for k in nums:
            count = 0
            if k not in visted:
                while True:
                    k = nums[k]
                    if k in visted:
                        break
                    else:
                        visted.add(k)
                    count += 1
                maximum = max(maximum, count)
            if N-len(visted) < maximum:
                break
        return maximum

    def arrayNesting(self, nums: List[int]) -> int:
        maximum = 1
        N = len(nums)
        for k in range(N):
            count = 0
            while nums[k] >= 0:
                oldK = k
                k = nums[k]
                nums[oldK] = -1

                count += 1
            maximum = max(maximum, count)
        return maximum


if __name__ == "__main__":
    nums = [5, 4, 0, 3, 1, 6, 2]
    output = Solution().arrayNesting(nums)
    print(output)
