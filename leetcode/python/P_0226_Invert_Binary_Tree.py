from typing import *
from datastructures.BinaryTree import *


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root


if __name__ == "__main__":
    bt = BinaryTree.bfsToTree([1, 2, 3])
    print(bt)
    Solution().invertTree(bt.root)
    print(bt)
