# Problem Link: https://leetcode.com/problems/intersection-of-two-linked-lists/



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

Runtime: 168 ms, faster than 61.94% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.7 MB, less than 28.96% of Python3 online submissions for Intersection of Two Linked Lists.
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next
        while headB:
            if headB in visited: return headB
            headB = headB.next
        return None



"""
Solution II: two pointers

Complexity Analysis:
- Time: O(N)
- Space: O(1)

Runtime: 159 ms, faster than 83.77% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.3 MB, less than 94.64% of Python3 online submissions for Intersection of Two Linked Lists.
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a