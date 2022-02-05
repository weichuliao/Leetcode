# Problem Link: https://leetcode.com/problems/boundary-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution I: rewrite from Java, but maximum recursion depth exceeded in comparison
class Solution:
    def isLeaf(self, node):
        return not node.left and not node.right
    
    def isRightBound(self, flag):
        return flag == 2
    
    def isLeftBound(self, flag):
        return flag == 1
    
    def isRoot(self, flag):
        return flag == 0
    
    def leftChildFlag(self, node, flag):
        if self.isLeftBound(flag) or self.isRoot(flag):
            return 1
        elif self.isRightBound(flag) and not node.right:
            return 2
        else: return 3
    
    def rightChildFlag(self, node, flag):
        if self.isRightBound(flag) or self.isRoot(flag):
            return 2
        elif self.isLeftBound(flag) and self.isRoot(flag):
            return 1
        else: return 3
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # only root, root is not in boundary
        if not root.left and not root.right:
            return []
        
        left_bound, right_bound, leaves = [], [], []
        
        def preorder(node, flag) -> None:
            if not node:
                return
            if self.isRightBound(flag):
                right_bound.append(node.val)
            elif self.isLeftBound(flag) or self.isRoot(flag):
                left_bound.append(node.val)
            elif self.isLeaf(node.val):
                leaves.append(node.val)
            preorder(root.left, self.leftChildFlag(node, flag))
            preorder(root.right, self.rightChildFlag(node, flag))
            return
        
        preorder(root, 0)
        return left_bound + leaves + right_bound



# Solution II:
# Reference: https://zhenyu0519.github.io/2020/03/13/lc545/
# Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Boundary of Binary Tree.
# Memory Usage: 16.4 MB, less than 41.88% of Python3 online submissions for Boundary of Binary Tree.
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None: return []
        res = [root.val]
        def leftBoundary(root):
            if root is None or root.left is None and root.right is None:
                return
            res.append(root.val)
            if root.left:
                leftBoundary(root.left)
            else:
                leftBoundary(root.right)

        def rightBoundary(root):
            if root is None or root.left is None and root.right is None:
                return
            if root.right:
                rightBoundary(root.right)
            else:
                rightBoundary(root.left)
            res.append(root.val)

        def leaves(node):
            if node is None:
                return
            if node.left is None and node.right is None and node != root:
                res.append(node.val)
            leaves(node.left)
            leaves(node.right)

        leftBoundary(root.left)
        leaves(root)
        rightBoundary(root.right)
        return res