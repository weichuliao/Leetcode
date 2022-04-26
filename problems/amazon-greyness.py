from typing import List

class Solution:
    def solution(self, pixel: List[List[int]]) -> int:
        rowGrey = [0] * len(pixel)
        colGrey = [0] * len(pixel[0])
        ans = float('-inf')
        for row in range(len(pixel)):
            for col in range(len(pixel[0])):
                # white
                if pixel[row][col] == 0:
                    rowGrey[row] -= 1
                # black
                else:
                    rowGrey[row] += 1
                ans = max(ans, rowGrey[row])
        for row in range(len(pixel[0])):
            for col in range(len(pixel)):
                # white
                if pixel[row][col] == 0:
                    colGrey[col] -= 1
                # black
                else:
                    colGrey[col] += 1
                ans = max(ans, rowGrey[row])
        return ans

execution = Solution()
result = execution.solution([[1, 0, 0, 1], [0, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1]])
print(result)