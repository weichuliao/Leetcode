# Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
Solution I:

Complexity Analysis:
- Time: 
- Space: 

Runtime: 44 ms, faster than 19.21% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.4 MB, less than 12.72% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
class Solution:
    def inorder(self, root, res):
        if not root:
            return
        
        root.left = self.inorder(root.left, res)
        res.append(root.val)
        root.right = self.inorder(root.right, res)
        return res
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.inorder(root, res)



"""
Solution II: recursion

Complexity Analysis:
- Time: 
- Space: 

"""
