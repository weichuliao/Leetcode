# Problem Link: https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Solution I:
# Runtime: 28 ms, faster than 98.33% of Python3 online submissions for Rotate List.
# Memory Usage: 14.4 MB, less than 27.40% of Python3 online submissions for Rotate List.
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head
        
        length = 1
        node = head
        while node.next != None:
            length += 1
            node = node.next
        
        if length == 1:
            return head
        
        target_pos = length - (k % length)
        target_node = None
        node = head
        while node.next != None:
            target_pos -= 1
            if (target_pos == 0):
                target_node = node
            node = node.next
            
        if target_node != None:
            node.next = head
            head = target_node.next
            target_node.next = None
        
        return head