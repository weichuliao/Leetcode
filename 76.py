# Problem Link: https://leetcode.com/problems/minimum-window-substring/



"""
Solution I: sliding window

Complexity Analysis:
- Time: O(S+T) where S denotes the length of string s and T the length of string t
- Space: O(S+T)

Runtime: 424 ms, faster than 13.59% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 15 MB, less than 28.19% of Python3 online submissions for Minimum Window Substring.
"""
from collections import Counter
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        ans = s + s
        n = len(s)
        target = Counter(t)
        counter = defaultdict(lambda: 0)

        def contains(counter, target):
            # 尚未達到字數，要 return False，持續擴展窗口 = r 向下一個移動
            if len(counter) < len(target): return False
            # 若達到字數，檢查目前窗口字數是否吻合目標 string t
            for k in counter:
                if counter[k] < target[k]: return False
            return True

        for r in range(n):
            # only focus on characters appearing among the string t
            if s[r] in target: counter[s[r]] += 1
            # 檢查窗口，若是當前窗口符合要求 = 涵蓋 string t，就變更 ans，或是縮小窗口（因為題目要的是最小）
            while l < n and contains(counter, target):
                if r - l + 1 < len(ans): ans = s[l:r+1]
                if s[l] in target: counter[s[l]] -= 1
                l += 1
        return "" if ans == s + s else ans