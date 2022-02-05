# Problem Link: https://leetcode.com/problems/middle-of-the-linked-list/submissions/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: 

Complexity Analysis:
- Time: O(N), where N is the number of nodes in the given list.
- Space: O(1), the space used by slow and fast. 

Runtime: 51 ms, faster than 12.30% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.1 MB, less than 91.85% of Python3 online submissions for Middle of the Linked List.
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow