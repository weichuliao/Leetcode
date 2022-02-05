# Problem Link: https://leetcode.com/problems/reverse-linked-list/



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

Runtime: 39 ms, faster than 53.22% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.6 MB, less than 77.22% of Python3 online submissions for Reverse Linked List.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev



"""
Solution II: recursion

Complexity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 70 ms, faster than 6.99% of Python3 online submissions for Reverse Linked List.
Memory Usage: 19 MB, less than 16.77% of Python3 online submissions for Reverse Linked List.
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        ans = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ans