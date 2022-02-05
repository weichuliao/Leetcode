# Problem Link: https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
# Runtime: 72 ms, faster than 23.09% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 19.2 MB, less than 22.21% of Python3 online submissions for Balanced Binary Tree.
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return max(l, r) + 1
        
        if not root: return True
        if abs(dfs(root.left) -  dfs(root.right)) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)