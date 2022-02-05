# Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: merge with divide and conquer

Complexity Analysis:
- Time: O(kn*logk)
- Space: O(logk)

Runtime: 116 ms, faster than 66.54% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.7 MB, less than 93.21% of Python3 online submissions for Merge k Sorted Lists.
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0: return None
        if n == 1: return lists[0]
        if n == 2: return self.mergeTwoLists(lists[0], lists[1])
        mid = n // 2
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:n]))
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        res = ListNode()
        node1, node2, node3 = list1, list2, res
        while node1 and node2:
            if node1.val <= node2.val:
                node3.next = node1
                node1 = node1.next
            else:
                node3.next = node2
                node2 = node2.next
            node3 = node3.next
        node3.next = node2 if not node1 else node1
        return res.next