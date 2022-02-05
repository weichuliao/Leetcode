# Problem Link: https://leetcode.com/problems/sudoku-solver/



"""
Solution I: hash set and backtracking

Complexity Analysis:
- Time: O(1) since the board size is fixed
- Space: O(1) since the board size is fixed

Runtime: 334 ms, faster than 54.47% of Python3 online submissions for Sudoku Solver.
Memory Usage: 14.2 MB, less than 86.50% of Python3 online submissions for Sudoku Solver.
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            return not (d in rows[row] or d in cols[col] or d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
        
        def remove_number(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'
        
        def place_next_numbers(row, col):
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)
        
        def backtrack(row = 0, col = 0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
        
        n = 3
        N = n * n
        box_index = lambda row, col: (row // n) * n + col // n
        rows = [defaultdict(int) for i in range(N)]
        cols = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)
        sudoku_solved = False
        backtrack()