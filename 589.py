# Problem Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""



"""
Solution I: iteration

Complexity Analysis:
- Time: we visit each node exactly once, and for each visit, the complexity of the operation (i.e. appending the child nodes) is proportional to the number of child nodes n (n-ary tree). Therefore the overall time complexity is O(N), where NN is the number of nodes, i.e. the size of tree.
- Space: depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(N).

Runtime: 44 ms, faster than 96.18% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.2 MB, less than 22.18% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output