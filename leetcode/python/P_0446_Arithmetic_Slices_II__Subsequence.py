from typing import List


class Solution:
    # TLE
    def subsetsBfs(self, nums: List[int]) -> List[List[int]]:
        allSubsets = [[]]
        for n in nums:
            size = len(allSubsets)
            for subIdx in range(size):
                curSubset = allSubsets[subIdx]
                if len(curSubset) < 2:
                    allSubsets.append(curSubset+[n])
                else:
                    if curSubset[1]-curSubset[0] == n - curSubset[-1]:
                        allSubsets.append(curSubset+[n])
        filteredSubsets = list(filter(lambda x: len(x) >= 3, allSubsets))
        print(filteredSubsets)
        return len(filteredSubsets)

    # TLE
    def subsetsDFS(self, nums: List[int]) -> List[List[int]]:
        def subsetsImpl(nums, lenOfNums, idx, temp):
            if idx < lenOfNums:
                if len(temp) < 2 or (len(temp) >= 2 and temp[1]-temp[0] == nums[idx]-temp[-1]):
                    subsetsImpl(nums, lenOfNums, idx+1, temp+[nums[idx]])
                subsetsImpl(nums, lenOfNums, idx+1, temp)

            else:
                if len(temp) > 2:
                    self.allSubsets.append(temp)
        self.allSubsets = []
        subsetsImpl(nums, len(nums), 0, [])
        print(self.allSubsets)
        return len(self.allSubsets)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        dp = [dict() for _ in nums]
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(0, i):
                diff = nums[i]-nums[j]
                # 2,2,3,4 , subset at 4 equal to , subsets at 3
                # i,e((2,3),(2,3)) + 4 and 3,4
                dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0)+1

                # if previous index that for any j , diff is same and has an
                # entry then we can use it result . else it means size of
                # subarray is less than 3
                if dp[j].get(diff, 0) > 0:
                    res += dp[j][diff]
            # print(dp)
        return res


if __name__ == "__main__":
    nums = [2, 4, 6, 8, 10]
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # nums = [ 7, 7, 7, 7]
    nums = [2, 2, 3, 4]
    output = Solution().subsets(nums)
    # [print(out) for out in output]
    print(output)
