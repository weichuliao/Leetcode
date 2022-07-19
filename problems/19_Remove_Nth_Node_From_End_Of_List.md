Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Solution I
maintain the n nodes apart between two pointers

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        for i in range(n + 1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
```

#### Complexity Analysis:
- Time: $O(L)$ where L denotes the length of the linked list.
- Space: $O(1)$