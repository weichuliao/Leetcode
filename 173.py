# Problem Link: https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
# Runtime: 75 ms, faster than 64.25% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 19.8 MB, less than 99.73% of Python3 online submissions for Binary Search Tree Iterator.
class BSTIterator:
    def inorder(self, root, arr):
        if not root: return
        root.left = self.inorder(root.left, arr)
        arr.append(root.val)
        root.right = self.inorder(root.right, arr)
        return arr

    def __init__(self, root: Optional[TreeNode]):
        self.arr = self.inorder(root, arr=[])
        self.root = root
        self.curidx = -1

    def next(self) -> int:
        self.curidx += 1
        return self.arr[self.curidx]

    def hasNext(self) -> bool:
        tmp = self.curidx + 1
        if tmp < len(self.arr):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()