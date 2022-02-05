# Problem Link: https://leetcode.com/problems/reverse-nodes-in-k-group/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Solution I: iterative

Complexity Analysis:
- Time: O(n), where n is number of Linked List
- Space: O(1)

Runtime: 66 ms, faster than 36.94% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.2 MB, less than 44.23% of Python3 online submissions for Reverse Nodes in k-Group.
"""
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode, terminal):
        cur = head
        pre = None
        while cur != terminal:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return tail, head
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # create a dummy node
        ans = ListNode()
        ans.next = head
        pre = ans
        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return ans.next
            next = tail.next
            head, tail = self.reverse(head, tail, tail.next)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = next
            pre = tail
            head = next
        return ans.next



"""
Solution II: recursion
"""