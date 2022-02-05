# Problem Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
# Runtime: 101 ms, faster than 17.80% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.7 MB, less than 58.80% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root