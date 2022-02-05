# Problem Link: https://leetcode.com/problems/find-bottom-left-tree-value/



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

Runtime: 32 ms, faster than 99.42% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 16.4 MB, less than 80.39% of Python3 online submissions for Find Bottom Left Tree Value.
"""
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None: return None
        queue = collections.deque([root])
        ans = None
        while queue:
            size = len(queue)
            for _ in range(size):
                ans = node = queue.popleft()
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
        return ans.val