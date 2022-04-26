from typing import List
from collections import defaultdict, Counter

class Solution:
    def solution(self, stockPrice: List[int], k: int) -> int:
        left = count = 0
        length = len(stockPrice)
        counter = Counter()
        ans = 0
        for right in range(len(stockPrice)):
            if counter[stockPrice[right]] == 0:
                k -= 1
            counter[stockPrice[right]] += 1
            while k < 0 or counter[stockPrice[right]] > 1:
                counter[stockPrice[left]] -= 1
                if counter[stockPrice[left]] == 0:
                    k += 1
                    counter.pop(stockPrice[left])
                left += 1
            if k == 0:
                ans = max(ans, sum(list(counter)))
        return ans if k == 0 else -1

execution = Solution()
assert execution.solution([10, 5, 188, 99, 99, 99, 99, 100, 10], 7) == -1
# print('The answer is', result)
assert execution.solution([1, 2, 7, 7, 4, 3, 6], 3) == 14
# print('The answer is', result)
assert execution.solution([1, 2, 4, 4], 4) == -1
# print('The answer is', result)