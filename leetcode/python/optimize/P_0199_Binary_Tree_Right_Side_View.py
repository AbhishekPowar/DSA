from datastructures import BinaryTree


class Solution:
    def rightSideView(self, root):
        ar = []

        def impl(root, level):
            if root:
                if len(ar) == level:
                    ar.append(root.val)
                impl(root.right, level + 1)
                impl(root.left, level + 1)
        impl(root, 0)
        return ar


if __name__ == "__main__":
    null = None
    # as of Sep 14 2021. bfsToTree has not been fixed. So please verify structure usign leetcode tree visualizer
    bt = BinaryTree.BinaryTree.bfsToTree(
        [1, 2, 3, 4])
    Solution().rightSideView(bt.root)
    print(bt)
