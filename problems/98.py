# Problem Link: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
# Runtime: 48 ms, faster than 51.98% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.9 MB, less than 24.19% of Python3 online submissions for Validate Binary Search Tree.
class Solution:
    def inorderTraversal(self, root, arr):
        if not root:
            return
        root.left = self.inorderTraversal(root.left, arr)
        arr.append(root.val)
        root.right = self.inorderTraversal(root.right, arr)
        return arr
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = self.inorderTraversal(root, arr=[])
        for i in range(1, len(arr)):
            if arr[i-1] >= arr[i]:
                return False
        return True


# Solution II:
# Runtime: 40 ms, faster than 91.06% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 17 MB, less than 24.19% of Python3 online submissions for Validate Binary Search Tree.
class Solution:
    prev = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not self.isValidBST(root.left):
            return False
        
        if root.val <= self.prev:
            return False
        
        self.prev = root.val
        
        return self.isValidBST(root.right)