# Problem Link: https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I: Recursion
# Runtime: 32 ms, faster than 66.24% of Python3 online submissions for Same Tree.
# Memory Usage: 14.2 MB, less than 61.47% of Python3 online submissions for Same Tree.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Solution II: BFS
# Runtime: 32 ms, faster than 66.24% of Python3 online submissions for Same Tree.
# Memory Usage: 14.3 MB, less than 30.08% of Python3 online submissions for Same Tree.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)
        
        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            
            if node1.val != node2.val: return False
            
            left1, left2 = node1.left, node2.left
            right1, right2 = node1.right, node2.right
            
            if (not left1) ^ (not left2): return False
            if (not right1) ^ (not right2): return False
            
            if left1: q1.append(left1)
            if left2: q2.append(left2)
            if right1: q1.append(right1)
            if right2: q2.append(right2)
        
        return not q1 and not q2


# Solution III: Preorder and Inorder Decide a Tree
# Runtime: 32 ms, faster than 66.24% of Python3 online submissions for Same Tree.
# Memory Usage: 14.4 MB, less than 30.08% of Python3 online submissions for Same Tree.
class Solution:
    def preorder(self, root, arr):
        if not root: 
            arr.append(" ")
            return arr

        arr.append(root.val)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)
        return arr
    
    def inorder(self, root, arr):
        if not root:
            arr.append(" ")
            return arr
        
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
        return arr
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pre1 = []
        pre1 = self.preorder(p, pre1)
        in1 = []
        in1 = self.inorder(p, in1)
        
        pre2 = []
        pre2 = self.preorder(q, pre2)
        in2 = []
        in2 = self.inorder(q, in2)
        
        return (pre1 == pre2) and (in1 == in2)