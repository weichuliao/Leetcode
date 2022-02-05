# Problem Link: https://leetcode.com/problems/binary-tree-postorder-traversal/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
Solution I: recursive traversal

Complexity Analysis:
- Time: 
- Space: 

Runtime: 35 ms, faster than 44.36% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.8 MB, less than 99.93% of Python3 online submissions for Binary Tree Postorder Traversal.
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, res):
            if not node: return
            node.left = dfs(node.left, res)
            node.right = dfs(node.right, res)
            res.append(node.val)
            return res
        return dfs(root, [])



"""
Solution II: iterative traversal
"""