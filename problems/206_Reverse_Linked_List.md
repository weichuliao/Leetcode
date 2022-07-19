# Problem Link: https://leetcode.com/problems/reverse-linked-list/

## Solution I: 
iterative

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
            # equals to below:
            # curr.next, prev, cur = prev, curr, curr.next
        return prev
```

#### Complexity Analysis:
- Time: $O(N)$
- Space: $O(1)$

<br>

## Solution II:
recursion

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        ans = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ans
```

#### Complexity Analysis:
- Time: $O(N)$
- Space: $O(N)$