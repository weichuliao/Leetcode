# Problem Link: https://leetcode.com/problems/palindrome-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: Copy into Array List and then Use Two Pointer Technique

Complexity Analysis:
- Time: O(n), where n is the number of nodes in the Linked List.
- Space: O(n), where n is the number of nodes in the Linked List.

Runtime: 824 ms, faster than 68.42% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 47.2 MB, less than 42.86% of Python3 online submissions for Palindrome Linked List.
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]