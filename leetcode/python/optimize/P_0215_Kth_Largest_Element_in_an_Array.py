from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def findLargestImpl(a, low, high, k):
            i = low
            j = high
            pivot = a[i]
            pivotIndex = i
            while i < j:
                while i <= high and a[i] >= pivot:
                    i += 1
                while j >= 0 and a[j] < pivot:
                    j -= 1
                if i < j:
                    a[i], a[j] = a[j], a[i]
            a[pivotIndex], a[j] = a[j], a[pivotIndex]
            if j == k:
                return a[k]
            elif j < k:
                findLargestImpl(a, j+1, high, k)
            else:
                findLargestImpl(a, low, j-1, k)
        k-=1
        N = len(nums)-1
        findLargestImpl(nums, 0, N, k)
        return nums[k]

