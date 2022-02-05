# Problem Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
# Runtime: 196 ms, faster than 28.96% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
# Memory Usage: 88.3 MB, less than 26.08% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder: 
            return None
        root = TreeNode(postorder[-1])
        
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        
        return root