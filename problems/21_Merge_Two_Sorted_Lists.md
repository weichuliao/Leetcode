# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/

## Solution I:
simulation / iteration

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
# revised as below:
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
```

#### Complexity Analysis:
- Time: $O(n + m)$
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

#### Complexity Analysis:
- Time: $O(n + m)$
- Space: $O(n + m)$