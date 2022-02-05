# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: Sentinel(哨兵) Head + Predecessor

Complexity Analysis:
- Time: O(N) since it's one pass along the input list.
- Space: O(1) because we don't allocate any additional data structure.

Runtime: 36 ms, faster than 93.71% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 14.4 MB, less than 26.18% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        pred = sentinel
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return sentinel.next