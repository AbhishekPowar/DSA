from functools import lru_cache


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        # leet code n ranges between 1 ot 8 for larger n use lru_cache to memoize
        # @lru_cache
        def arrayToTree(low, high):
            if low <= high:
                output = []
                for i in range(low, high+1):
                    leftTreeArr = arrayToTree(low, i-1)
                    rightTreeArr = arrayToTree(i+1, high)
                    for leftTree in leftTreeArr:
                        for rightTree in rightTreeArr:
                            output.append(
                                TreeNode(i, leftTree, rightTree))
                return output
            else:
                return [None]
        output = arrayToTree(1, n)
        return output


if __name__ == "__main__":
    n = 13 
    output = Solution().generateTrees(n)
    print(len(output))
