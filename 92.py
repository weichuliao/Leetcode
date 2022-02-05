# Problem Link: https://leetcode.com/problems/reverse-linked-list-ii/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: iterative

Complexity Analysis:
- Time: O(N) considering the list consists of N nodes. We process each of the nodes at most once (we don't process the nodes after the nth node from the beginning.
- Space: O(1) since we simply adjust some pointers in the original linked list and only use O(1) additional memory for achieving the final result.

Runtime: 32 ms, faster than 76.11% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 14.2 MB, less than 90.54% of Python3 online submissions for Reverse Linked List II.
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return None
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1
        tail, con = cur, prev
        while right:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            right -= 1
        if con: con.next = prev
        else: head = prev
        tail.next = cur
        return head