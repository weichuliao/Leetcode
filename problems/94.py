# Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/



"""
Solution I: recursion / DFS

Complexity Analysis:
- Time: O(n)
- Space: O(n)

Runtime: 44 ms, faster than 19.21% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.4 MB, less than 12.72% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
Solution II: iterative method

Complexity Analysis:
- Time: O(n)
- Space: O(n)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        return ans