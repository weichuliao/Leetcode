# Problem Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
# Runtime: 52 ms, faster than 77.57% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
# Memory Usage: 14.3 MB, less than 67.17% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        if len(preorder) == 1:
            return node
        
        i = postorder.index(preorder[1])
        node.left = self.constructFromPrePost(preorder[1:i+2], postorder[:i+1])
        node.right = self.constructFromPrePost(preorder[i+2:], postorder[i+1:-1])
        
        return node