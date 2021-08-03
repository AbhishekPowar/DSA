# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
class Solution:
    def subsetsWithDup(self, nums):
        '''Return list of subsets'''
        output = set()

        def subsetsWithDupImpl(nums, temp):
            if nums:
                subsetsWithDupImpl(nums[1:], temp[:]+[nums[0]])
                subsetsWithDupImpl(nums[1:], temp[:])
            else:
                output.add(tuple(temp))
        subsetsWithDupImpl(sorted(nums), [])
        return output


def main():
    ar = [1, 2, 3]
    output = Solution().subsetsWithDup(ar)
    print(output)


if __name__ == "__main__":
    main()
