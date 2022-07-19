Problem Link: https://leetcode.com/problems/number-of-islands
Explanation: https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-shu-liang-by-leetcode/

## Solution I
DFS

```python
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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1': return
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
```

#### Complexity Analysis:
- Time: $O(MN)$ where M denotes the number of columns and N the number of rows
- Space: $O(MN)$，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 MN

<br>

## Solution II
BFS

```python
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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(row, col):
            q = deque()
            q.append((row, col))  # first cell of each island
            visited.add((row, col))

            while q:
                r, c = q.popleft()  # FIFO

                # check neighbors in order of right, left, up, and down
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (0 <= (r + dr) < rows and
                       0 <= (c + dc) < cols and
                       grid[r + dr][c + dc] == "1" and
                       (r + dr, c + dc) not in visited):
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    bfs(row, col)
                    
        return islands
```

#### Complexity Analysis:
- Time: $O(MN)$ where M denotes the number of columns and N the number of rows
- Space: $O(min(M,N))$，在最坏情况下，整个网格均为陆地，队列的大小可以达到 min(M,N)

<br>

## Solution III
Union Find

```python
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
```

#### Complexity Analysis:
- Time: $O(MN×α(MN))$，其中 M 和 N 分别为行数和列数。注意当使用路径压缩（见 find 函数）和按秩合并（见数组 rank）实现并查集时，单次操作的时间复杂度为 α(MN)，其中 α(x) 为反阿克曼函数，当自变量 x 的值在人类可观测的范围内（宇宙中粒子的数量）时，函数 α(x) 的值不会超过 5，因此也可以看成是常数时间复杂度。
- Space: $O(MN)$，这是并查集需要使用的空间。i