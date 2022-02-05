# Problem Link: https://leetcode.com/problems/spiral-matrix-ii/


# Solution I: Simulation
# Runtime: 24 ms, faster than 97.32% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 14.4 MB, less than 17.94% of Python3 online submissions for Spiral Matrix II.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for x in range(n)] for y in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # directions: right, down, left, up
        row, col, cur_dir = 0, 0, 0
        for i in range(n*n):
            matrix[row][col] = i + 1
            dx, dy = dirs[cur_dir]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                cur_dir = (cur_dir + 1) % 4
                dx, dy = dirs[cur_dir]
            row, col = row + dx, col + dy
        return matrix


# Solution II: 一層一層simulation
# Runtime: 24 ms, faster than 97.32% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 14.4 MB, less than 48.59% of Python3 online submissions for Spiral Matrix II.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for x in range(n)] for y in range(n)]
        num = 1
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            for row in range(top + 1, bottom + 1):
                matrix[row][right] = num
                num += 1
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    matrix[bottom][col] = num
                    num += 1
                for row in range(bottom, top, -1):
                    matrix[row][left] = num
                    num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix