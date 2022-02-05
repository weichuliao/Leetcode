# Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I: Recursion
# Runtime: 32 ms, faster than 98.09% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.1 MB, less than 60.90% of Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))