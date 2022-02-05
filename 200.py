# Problem Link: https://leetcode.com/problems/number-of-islands
# Explanation: https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-shu-liang-by-leetcode/


"""
Solution I: DFS

Complexity Analysis:
- Time: O(MN) where M denotes the number of columns and N the number of rows
- Space: O(MN)，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 MN

Runtime: 300 ms, faster than 83.59% of Python3 online submissions for Number of Islands.
Memory Usage: 17 MB, less than 31.90% of Python3 online submissions for Number of Islands.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            grid[r][c] = 0
            rows, cols = len(grid), len(grid[0])
            for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                    dfs(grid, x, y)
            
        rows = len(grid)
        if rows == 0: return 0
        cols, islands = len(grid[0]), 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(grid, r, c)
        return islands



"""
Solution II: BFS

Complexity Analysis:
- Time: O(MN) where M denotes the number of columns and N the number of rows
- Space: O(min(M,N))，在最坏情况下，整个网格均为陆地，队列的大小可以达到 min(M,N)

Runtime: 402 ms, faster than 24.71% of Python3 online submissions for Number of Islands.
Memory Usage: 16.5 MB, less than 93.43% of Python3 online submissions for Number of Islands.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0: return 0
        cols = len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"
        return islands



"""
Solution III: Union Find

Complexity Analysis:
- Time: O(MN×α(MN))，其中 M 和 N 分别为行数和列数。注意当使用路径压缩（见 find 函数）和按秩合并（见数组 rank）实现并查集时，单次操作的时间复杂度为 α(MN)，其中 α(x) 为反阿克曼函数，当自变量 x 的值在人类可观测的范围内（宇宙中粒子的数量）时，函数 α(x) 的值不会超过 5，因此也可以看成是常数时间复杂度。
- Space: O(MN)，这是并查集需要使用的空间。

Runtime: 507 ms, faster than 10.11% of Python3 online submissions for Number of Islands.
Memory Usage: 19.1 MB, less than 26.25% of Python3 online submissions for Number of Islands.
"""
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1
    
    def getCount(self):
        return self.count
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0: return 0
        cols = len(grid[0])
        uf = UnionFind(grid)
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                            uf.union(r * cols + c, x * cols + y)
        return uf.getCount()