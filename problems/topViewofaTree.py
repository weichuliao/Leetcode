# Problem Link: https://binarysearch.com/problems/Top-View-of-a-Tree

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution I:
class Solution:
    def solve(self, root):
        q = collections.deque([(root, 0)])
        d = {}
        while q:
            cur, pos = q.popleft()
            if pos not in d:
                d[pos] = cur.val
            if cur.left:
                q.append((cur.left, pos - 1))
            if cur.right:
                q.append((cur.right, pos + 1))
        return list(map(lambda x: x[1], sorted(d.items(), key=lambda x: x[0])))