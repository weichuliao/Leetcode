# Problem Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/



"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""



"""
Solution I: level order traversal

Complexity Analysis:
- Time: O(N) since we process each node exactly once. Note that processing a node in this context means popping the node from the queue and then establishing the next pointers.
- Space: O(N). This is a perfect binary tree which means the last level contains N/2 nodes. The space complexity for breadth first traversal is the maximum space occupied and the space occupied by the queue is dependent upon the maximum number of nodes in particular level. So, in this case, the space complexity would be O(N).

Runtime: 52 ms, faster than 66.08% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 15.5 MB, less than 51.96% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root



"""
Solution II: using previously established next pointers

Complexity Analysis:
- Time: 
- Space: 


"""
