# Problem Link: https://leetcode.com/problems/partition-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: 

Complexity Analysis:
- Time: O(N)
- Space: O(1)

Runtime: 36 ms, faster than 75.71% of Python3 online submissions for Partition List.
Memory Usage: 14.1 MB, less than 84.53% of Python3 online submissions for Partition List.
"""
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dum1, dum2 = ListNode(), ListNode()
        dum1_head, dum2_head = dum1, dum2
        while head:
            if head.val < x:
                dum1.next = head
                dum1 = dum1.next
            else:
                dum2.next = head
                dum2 = dum2.next
            head = head.next
        dum2.next = None
        dum1.next = dum2_head.next
        return dum1_head.next