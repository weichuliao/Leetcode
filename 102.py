# Problem Link: https://leetcode.com/problems/binary-tree-level-order-traversal/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
Solution I: recursion

Complexity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 42 ms, faster than 43.94% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.8 MB, less than 24.58% of Python3 online submissions for Binary Tree Level Order Traversal.
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        result = []
        def addToResult(level, node):
            if level > len(result) - 1:
                result.append([])
            result[level].append(node.val)
            if node.left: addToResult(level+1, node.left)
            if node.right: addToResult(level+1, node.right)
        addToResult(0, root)
        return result



"""
Solution II: iteration

Complexity Analysis:
- Time: 
- Space: 


"""