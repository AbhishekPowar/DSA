class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'


class BinaryTree():
    def __init__(self):
        self.root = None

    def add(self, val=0, left=None, right=None):
        #will be added soon
        pass

    @staticmethod
    def printTree(root, indent=4, level=0, empty='null'):
        space = ' '*(indent*level)
        if root:
            main = f"{space}{root}"
            level += 1
            left = BinaryTree.printTree(root.left, indent, level, empty)
            right = BinaryTree.printTree(root.right, indent, level, empty)
            result = '\n'.join(right.split('\n')[::-1])
            result += '\n' + main + '\n' + left
            return result
        return f"{space}{empty}"

    def __str__(self):
        return BinaryTree.printTree(self.root)

    @staticmethod
    def bfsToTree(bfsArray):
        treeNodes = []
        for val in bfsArray:
            if val is None:
                treeNodes.append(None)
            else:
                treeNodes.append(TreeNode(val))
        N = len(treeNodes)
        validIdx = 0
        for treeNode in treeNodes:
            if treeNode is not None:
                leftIdx = validIdx * 2 + 1
                rightIdx = validIdx * 2 + 2

                if leftIdx < N:
                    treeNode.left = treeNodes[leftIdx]
                if rightIdx < N:
                    treeNode.right = treeNodes[rightIdx]
                validIdx += 1

        tree = BinaryTree()
        tree.root = treeNodes[0]
        return tree


if __name__ == "__main__":
    null = None
    bt = BinaryTree.bfsToTree([1, 2, 3, 4])
    print(bt)
    print('end')
