# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: 

Complexity Analysis:
- Time: O(n). Because each node in the list is checked exactly once to determine if it is a duplicate or not, the total run time is O(n), where n is the number of nodes in the list.
- Space: O(1). No additional space is used.

Runtime: 63 ms, faster than 26.00% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.2 MB, less than 56.92% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return sentinel.next