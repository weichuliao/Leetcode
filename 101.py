# Problem Link: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution I: Recursion
# Runtime: 36 ms, faster than 61.58% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 14.3 MB, less than 79.11% of Python3 online submissions for Symmetric Tree.
class Solution:
    def recursion(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.recursion(p.left, q.right) and self.recursion(p.right, q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        return self.recursion(p, q)