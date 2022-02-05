# Problem Link: https://leetcode.com/problems/n-queens-ii/


# Solution: From NTHU Programming I Class, using three arrays to store the conditions
# Runtime: 40 ms, faster than 96.54% of Python3 online submissions for N-Queens II.
# Memory Usage: 14.4 MB, less than 14.11% of Python3 online submissions for N-Queens II.
class Solution:
    ans = 0
    col = [0 for _ in range(50)]
    cnt = [0 for _ in range(50)]
    cnt2 = [0 for _ in range(50)]
    def totalNQueens(self, n: int) -> int:
        def placeQueens(row):
            if row == n:
                self.ans += 1
            else:
                for i in range(n):
                    if self.col[i] == 0 and self.cnt[row - i] == 0 and self.cnt2[row + i] == 0:
                        self.col[i] = 1
                        self.cnt[row - i] = 1
                        self.cnt2[row + i] = 1
                        placeQueens(row + 1)
                        self.col[i] = 0
                        self.cnt[row - i] = 0
                        self.cnt2[row + i] = 0
        placeQueens(0)
        return self.ans


# Solution II: From Leetcode++, using three sets to store the conditions
# Runtime: 40 ms, faster than 96.54% of Python3 online submissions for N-Queens II.
# Memory Usage: 14.4 MB, less than 35.64% of Python3 online submissions for N-Queens II.
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    count += backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                return count
                    
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        return backtrack(0)