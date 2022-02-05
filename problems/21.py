# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: simulation

Complexity Analysis:
- Time: O(n)
- Space: O(n)

Runtime: 46 ms, faster than 39.48% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.4 MB, less than 31.45% of Python3 online submissions for Merge Two Sorted Lists.
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2, head = list1, list2, ListNode()
        ans = head
        while node1 or node2:
            if node1 and not node2:
                head.next = node1
                head = head.next
                node1 = node1.next
            elif node2 and not node1:
                head.next = node2
                head = head.next
                node2 = node2.next
            elif node1.val < node2.val:
                head.next = node1
                head = head.next
                node1 = node1.next
            elif node1.val > node2.val:
                head.next = node2
                head = head.next
                node2 = node2.next
            elif node1.val == node2.val:
                head.next = node1
                head = head.next
                node1 = node1.next
                head.next = node2
                head = head.next
                node2 = node2.next
        return ans.next
"""
revised as below:

Runtime: 40 ms, faster than 64.93% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.3 MB, less than 62.23% of Python3 online submissions for Merge Two Sorted Lists.
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ans = head
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list2 if not list1 else list1
        return ans.next



"""
Solution II: recursion
"""