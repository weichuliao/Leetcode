# Problem Link: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: prefix sum + hash map

Complexity Analysis:
- Time: O(N+N)
- Space: O(N)

Runtime: 42 ms, faster than 74.86% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
Memory Usage: 14.5 MB, less than 81.56% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
"""
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = collections.defaultdict(ListNode)
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        presum = 0
        while node:
            presum += node.val
            hashmap[presum] = node
            node = node.next
            
        presum = 0
        node = dummy
        while node:
            presum += node.val
            node.next = hashmap[presum].next
            node = node.next
            
        return dummy.next