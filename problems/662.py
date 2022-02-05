# Problem Link: https://leetcode.com/problems/maximum-width-of-binary-tree/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
Solution I: bfs traversal

Complexity Analysis:
- Time: O(N). We visit each node once and only once. And at each visit, it takes a constant time to process.
- Space: O(N). 
    - We used a queue to maintain the nodes along with its indices, which is the main memory consumption of the algorithm.
    - Due to the nature of BFS, at any given moment, the queue holds no more than two levels of nodes. In the worst case, a level in a full binary tree contains at most half of the total nodes (i.e. N/2), i.e. this is also the level where the leaf nodes reside.
    - Hence, the overall space complexity of the algorithm is O(N).

Runtime: 46 ms, faster than 60.56% of Python3 online submissions for Maximum Width of Binary Tree.
Memory Usage: 14.9 MB, less than 83.01% of Python3 online submissions for Maximum Width of Binary Tree.
"""
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0
        queue = deque()
        queue.append((root, 0))
        while queue:
            level_length = len(queue)
            _, level_head_idx = queue[0]
            for _ in range(level_length):
                node, col_idx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * col_idx))
                if node.right:
                    queue.append((node.right, 2 * col_idx + 1))
            max_width = max(max_width, col_idx - level_head_idx + 1)
        return max_width



"""
Solution II: dfs traversal

Complexity Analysis:
- Time: 
- Space: 


"""
