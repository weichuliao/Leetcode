from typing import List
from math import floor

class Solution:
    def findEarliestMonth(self, stockPrice: List[int], n: int) -> int:
        prefix = [sum(stockPrice[:i+1]) for i in range(n)]
        minMonth = 0
        minPrice = float('inf')
        for i in range(n - 1):
            newMinPrice = abs(floor(prefix[i] / (i + 1)) - floor((prefix[n-1] - prefix[i]) / (n - 1 - i)))
            if minPrice > newMinPrice:
                minPrice = newMinPrice
                minMonth = i + 1
        return minMonth

execution = Solution()
assert execution.findEarliestMonth([1, 3, 2, 4, 5], 5) == 2
assert execution.findEarliestMonth([1, 1, 1, 1, 1, 1], 6) == 1
assert execution.findEarliestMonth([11, 9, 4, 8, 1, 10], 6) == 3