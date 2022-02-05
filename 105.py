# Problem Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
# Runtime: 184 ms, faster than 41.58% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 88.1 MB, less than 27.42% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        
        i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        
        return root