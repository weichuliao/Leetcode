# Problem Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
# Runtime: 32 ms, faster than 93.08% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 14.2 MB, less than 74.06% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
class Solution:
    def constructTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        
        i = inorder.index(root.val)
        root.left = self.constructTree(preorder[1:i+1], inorder[:i])
        root.right = self.constructTree(preorder[i+1:], inorder[i+1:])
        
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = preorder.copy()
        inorder.sort()
        return self.constructTree(preorder, inorder)
        