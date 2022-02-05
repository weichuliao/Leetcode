# Problem Link: https://leetcode.com/problems/sort-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: top-down merge sort

Complexity Analysis:
- Time: O(nlogn), where n is the number of nodes in linked list. The algorithm can be split into 2 phases, Split and Merge.
- Space: O(logn) , where n is the number of nodes in linked list. Since the problem is recursive, we need additional space to store the recursive call stack. The maximum depth of the recursion tree is logn.

Runtime: 484 ms, faster than 57.49% of Python3 online submissions for Sort List.
Memory Usage: 30.2 MB, less than 72.56% of Python3 online submissions for Sort List.
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def merge(self, list1: ListNode, list2: ListNode):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next
    
    def getMid(self, head):
        midPrev = None
        while head and head.next:
            midPrev = head if midPrev is None else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid



"""
Solution II: bottom-up merge sort

Complexity Analysis:
- Time: 
- Space: 


"""
