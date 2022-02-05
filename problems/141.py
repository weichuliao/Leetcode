# Problem Link: https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



"""
Solution I: Floyd's

Complexity Analysis:
- Time: O(n). Let us denote n as the total number of nodes in the linked list. To analyze its time complexity, we consider the following two cases separately.

    List has no cycle:
    The fast pointer reaches the end first and the run time depends on the list's length, which is O(n).

    List has a cycle:
    We break down the movement of the slow pointer into two steps, the non-cyclic part and the cyclic part:

    The slow pointer takes "non-cyclic length" steps to enter the cycle. At this point, the fast pointer has already reached the cycle. 
    Number of iterations = non-cyclic length = N

    Both pointers are now in the cycle. Consider two runners running in a cycle - the fast runner moves 2 steps while the slow runner moves 1 steps at a time. Since the speed difference is 1, it takes 
            (distance between the 2 runners) / difference of speed
        loops for the fast runner to catch up with the slow runner. As the distance is at most "cyclic length K" and the speed difference is 1, we conclude that
            Number of iterations = almost "cyclic length K".

        Therefore, the worst case time complexity is O(N+K), which is O(n).

- Space: O(1). We only use two nodes (slow and fast) so the space complexity is O(1).

Runtime: 72 ms, faster than 38.42% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.7 MB, less than 24.41% of Python3 online submissions for Linked List Cycle.
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None: return False
            slow = slow.next
            fast = fast.next.next
        return True



"""
Solution II: hash table

Runtime: 58 ms, faster than 54.16% of Python3 online submissions for Linked List Cycle.
Memory Usage: 18.1 MB, less than 7.78% of Python3 online submissions for Linked List Cycle.
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head is not None:
            if head in seen: return True
            seen.add(head)
            head = head.next
        return False