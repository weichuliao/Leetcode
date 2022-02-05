# Problem Link: https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
# Runtime: 344 ms, faster than 77.40% of Python3 online submissions for Balance a Binary Search Tree.
# Memory Usage: 21.3 MB, less than 7.86% of Python3 online submissions for Balance a Binary Search Tree.
class Solution:
    def inorder(self, node):
        if not node: return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.inorder(root)
        def dfs(start, end):
            if start == end: return TreeNode(nums[start])
            if start > end: return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(start, mid - 1)
            root.right = dfs(mid + 1, end)
            return root
        return dfs(0, len(nums) - 1)