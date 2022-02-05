# Problem Link: https://leetcode.com/problems/fruit-into-baskets/



"""
Solution I:

Complexity Analysis: sliding window
- Time: O(N)
- Space: O(N)

Runtime: 784 ms, faster than 75.13% of Python3 online submissions for Fruit Into Baskets.
Memory Usage: 20.3 MB, less than 33.21% of Python3 online submissions for Fruit Into Baskets.
"""
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, ans = 0, 0
        picked = defaultdict(lambda: 0)
        for r in range(len(fruits)):
            picked[fruits[r]] += 1
            while len(picked) > 2:
                ans = max(ans, r - l)
                if picked[fruits[l]] > 1: picked[fruits[l]] -= 1
                else: del picked[fruits[l]]
                l += 1
        return max(ans, sum(picked.values()))
"""
slightly revised as below:

Complexity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 976 ms, faster than 33.85% of Python3 online submissions for Fruit Into Baskets.
Memory Usage: 20.2 MB, less than 33.19% of Python3 online submissions for Fruit Into Baskets.
"""
from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, ans = 0, 0
        picked = Counter()
        for r, fruit in enumerate(fruits):
            picked[fruit] += 1
            while len(picked) > 2:
                picked[fruits[l]] -= 1
                if picked[fruits[l]] == 0: del picked[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans



"""
Solution II: prefix sum

Complexity Analysis:
- Time: O(N) where N denotes the length of fruits
- Space: O(k)

Runtime: 1377 ms, faster than 11.34% of Python3 online submissions for Fruit Into Baskets.
Memory Usage: 20.4 MB, less than 6.65% of Python3 online submissions for Fruit Into Baskets.
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def atMostK(k, nums):
            i = ans = 0
            win = collections.defaultdict(lambda: 0)
            for j in range(len(nums)):
                if win[nums[j]] == 0: k -= 1
                win[nums[j]] += 1
                while k < 0:
                    win[nums[i]] -= 1
                    if win[nums[i]] == 0: k += 1
                    i += 1
                ans = max(ans, j - i + 1)
            return ans
        return atMostK(2, fruits)