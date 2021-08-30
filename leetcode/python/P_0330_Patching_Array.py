# https://www.youtube.com/watch?v=N-tcCOCNSZY&ab_channel=CodingDecoded
from typing import List
from collections import Counter

class Solution:

    def minPatches(self, nums: List[int], n: int) -> int:
        reach = 0
        index = 0
        count = 0
        lenOfNums = len(nums)
        while reach < n:
            if index == lenOfNums or nums[index] > (reach+1):
                reach = reach * 2 + 1
                count += 1
            elif index < lenOfNums:
                reach += nums[index]
                index += 1
        return count

    def minPatchesUgly(self, nums: List[int], n: int) -> int:
        curHigh = 0
        count = 0
        for x in nums:
            while curHigh+1 < x and curHigh < n:
                curHigh, count = 2 * curHigh + 1, count+1
            if curHigh >= n:
                return count
            curHigh += x
        while curHigh < n:
            curHigh, count = 2 * curHigh + 1, count+1
        return count

    def minPatchesBruteForce(self, nums: List[int], n: int) -> int:
        def populate(charMap, nums):
            for n in range(1, len(nums)+2):
                binaryStr = bin(n)[2:].zfill(len(nums))
                tempSum = 0
                tempAr = []
                for index, bit in enumerate(binaryStr):
                    if bit == '1':
                        tempSum += nums[int(index)]
                        tempAr.append(nums[int(index)])
                charMap[tempSum] = tempAr

        def calculateForEmpty(charMap, nums):
            for key in charMap:
                if charMap[key] == []:
                    for distance in range(1, key+1):
                        if distance == key:
                            self.total = Counter(nums+[key])
                            self.patch.append(key)
                            charMap[key] = [key]
                            break
                        else:
                            keyMinusDistance = key-distance
                            if distance in (self.total-Counter(charMap[keyMinusDistance])):
                                charMap[key] = charMap[keyMinusDistance] + \
                                    [distance]
                                break

        self.total = Counter(nums)
        self.patch = []
        charMap = {i: [] for i in range(1, n+1)}
        populate(charMap, nums)
        calculateForEmpty(charMap, nums)

        print(self.patch)
        return len(self.patch)


if __name__ == "__main__":
    nums = [1, 3]
    n = 16
    output = Solution().minPatches(nums, n)
    print(output)
