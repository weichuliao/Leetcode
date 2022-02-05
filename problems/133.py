# Problem Link: https://leetcode.com/problems/clone-graph/
# Explanation: https://leetcode-cn.com/problems/clone-graph/solution/ke-long-tu-by-leetcode-solution/



"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""



"""
Solution I: DFS

Runtime: 32 ms, faster than 94.40% of Python3 online submissions for Clone Graph.
Memory Usage: 14.6 MB, less than 83.56% of Python3 online submissions for Clone Graph.
"""
class Solution(object):
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        if node in self.visited:
            return self.visited[node]
        clone = Node(node.val, [])
        self.visited[node] = clone
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone



"""
Solution II: BFS

Complexity Analysis:
- Time: O(N)，其中 N 表示节点数量。广度优先搜索遍历图的过程中每个节点只会被访问一次。
- Space: O(N)。哈希表使用 O(N) 的空间。广度优先搜索中的队列在最坏情况下会达到 O(N) 的空间复杂度，因此总体空间复杂度为 O(N)。

Runtime: 57 ms, faster than 10.06% of Python3 online submissions for Clone Graph.
Memory Usage: 14.8 MB, less than 5.18% of Python3 online submissions for Clone Graph.
"""
from collections import deque
class Solution(object):    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])
        
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if n not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        
        return visited[node]