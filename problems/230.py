# Problem Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
Solution I: recursive inorder traversal

Complexity Analysis:
- Time: O(N) to build a traversal.
- Space: O(N) to keep an inorder traversal.

Runtime: 56 ms, faster than 61.07% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.3 MB, less than 16.44% of Python3 online submissions for Kth Smallest Element in a BST.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        return inorder(root)[k-1]



"""
Solution II: iterative inorder traversal
"""



"""
Solution III:

Runtime: 32 ms, faster than 99.92% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.1 MB, less than 59.58% of Python3 online submissions for Kth Smallest Element in a BST.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def nodeCount(node):
            if not node: return 0
            l = nodeCount(node.left)
            r = nodeCount(node.right)
            return 1 + l + r
        
        c = nodeCount(root.left)
        if c == k - 1: return root.val
        elif c < k - 1: return self.kthSmallest(root.right, k - c - 1)
        return self.kthSmallest(root.left, k)