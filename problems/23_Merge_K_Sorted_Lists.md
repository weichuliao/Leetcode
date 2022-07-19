# Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/

## Solution I:
brute force

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode()
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for i in sorted(nodes):
            point.next = ListNode(i)
            point = point.next
        return head.next
```

#### Complexity Analysis:
- Time: $O(nlogn)$ for sorting dominating the algorithm.
- Space: $O(n)$ for creating a new linked list.

<br>

## Solution II
compare value one by one

```python

```

#### Complexity Analysis:
- Time: $O(kn)$
- Space: $O(n)$ for creating a new linked list or $O(1)$ for merging lists in-place.

<br>

## Solution III
compare value one by one with priority queue (implemented with heapq in Python)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        # using idx to avoid comparison error in heapify()
        for idx, node in enumerate(lists):
            if node: queue.append((node.val, idx, node))
        heapq.heapify(queue)
        
        head = point = ListNode()
        while queue:
            val, idx, node = heapq.heappop(queue)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node: heapq.heappush(queue, (node.val, idx, node))
        return head.next
```

#### Complexity Analysis:
- Time: $O(Nlogk)$ where k is the number of linked lists. $O(logk)$ for every pop and insertion to priority queue, and there are N nodes.
- Space: $O(n)$ for creating a new linked list and $O(k)$ for keeping a priority queue (implemented with heaps).

<br>

## Solution IV
merge lists one by one

```python

```

#### Complexity Analysis:
- Time: $O(kn)$
- Space: $O(1)$ for merging two lists in-place.

<br>

## Solution V:
merge with divide and conquer

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
```

#### Complexity Analysis:
- Time: $O(nlogk)$
- Space: $O(logk)$