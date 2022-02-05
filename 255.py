# Problem Link: https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/



"""
Solution: Monotonic stack

1. if the elements added into stack is in a decreasing order, it means the elements are in the left subtree.
2. if the element are larger than the top element in the stack, it means the elements are in the right subtree.
   2-1. we have to pop out all the elements smaller than the element to be added.
   2-2. at the same time, renew the value of the min_val variable by elements that popped out.
        2-2-1. if the element to be added to stack is smaller the min_val, the preorder list is wroing.

Complexity Analysis
Time: Since the elements of input are only appended and popped at motst one time,
      the time complexity is O(N) where N denotes the length of input
Space: Since stack is used and its size is the same as that of the input list,
       the space complexity is O(N) where N denotes the length of input list

Runtime: 220 ms, faster than 83.61% of Python3 online submissions for Verify Preorder Sequence in Binary Search Tree.
Memory Usage: 14.9 MB, less than 97.39% of Python3 online submissions for Verify Preorder Sequence in Binary Search Tree.
"""
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if len(preorder) == 1:
            return True
        stack = []
        min_val = float('-inf')
        for node in preorder:
            if node < min_val:
                    return False
            while stack and node > stack[-1]:
                min_val = stack.pop()
            stack.append(node)
        return True