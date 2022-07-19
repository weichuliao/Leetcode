from typing import List

class Solution:
    def solution(self, n: int, tempChange: List[int]) -> int:
        ans = float('-inf')
        prefix = [sum(tempChange[:i+1]) for i in range(len(tempChange))]
        for i in range(n):
            if i == 0:
                ans = max(ans, prefix[i], prefix[n-1])
            else:
                ans = max(ans, prefix[i], (prefix[n-1] - prefix[i-1]))
        return ans

execution = Solution()
result = execution.solution(3, [6, -2, 5])
print('The answer is', result)
result = execution.solution(3, [-1, 2, 3])
print('The answer is', result)
result = execution.solution(1, [-30])
print('The answer is', result)
result = execution.solution(10, [-30, 5, 8, 1200, 3432, 341, 67, 30, 4, -33422])
print('The answer is', result)
result = execution.solution(4, [5, 10, -30, 18])
print('The answer is', result)