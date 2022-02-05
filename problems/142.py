# Problem Link: https://leetcode.com/problems/linked-list-cycle-ii/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



"""
Solution I: hash table

Complexity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 47 ms, faster than 91.30% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.8 MB, less than 11.46% of Python3 online submissions for Linked List Cycle II.
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        while head:
            if head in visited: return head
            visited.add(head)
            head = head.next
        return None