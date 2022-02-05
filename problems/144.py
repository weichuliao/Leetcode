# Problem Link: https://leetcode.com/problems/binary-tree-preorder-traversal/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
Solution I: stack

Complexity Analysis:
- Time: we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes, i.e. the size of tree.
- Space: depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(N).

Runtime: 19 ms, faster than 99.49% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 14 MB, less than 91.52% of Python3 online submissions for Binary Tree Preorder Traversal.
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return output



"""
Solution II: recursion

42 ms, faster than 33.97% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 14.2 MB, less than 47.59% of Python3 online submissions for Binary Tree Preorder Traversal.
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node, res):
            if not node:
                return
            res.append(node.val)
            node.left = preorder(node.left, res)
            node.right = preorder(node.right, res)
            return res
        res = []
        return preorder(root, res)