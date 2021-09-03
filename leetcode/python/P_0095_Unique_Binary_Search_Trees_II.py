from functools import lru_cache
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        def arrayToTree(nums):
            if nums:
                output = []
                for i in range(len(nums)):
                    leftTreeArr = arrayToTree(nums[:i])
                    rightTreeArr = arrayToTree(nums[i+1:])
                    for leftTree in leftTreeArr:
                        for rightTree in rightTreeArr:
                            output.append(
                                TreeNode(nums[i], leftTree, rightTree))
                return output
            else:
                return [None]
        nums = [i for i in range(1,n+1)]
        output = arrayToTree(nums)
        return output


if __name__ == "__main__":
    n = 3
    output = Solution().generateTrees(n)
    print(output)
