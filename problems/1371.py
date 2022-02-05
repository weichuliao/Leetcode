# Problem Link: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
# Reference: https://github.com/azl397985856/leetcode/blob/master/problems/1371.find-the-longest-substring-containing-vowels-in-even-counts.md



"""
Solution I: prefix sum and prune

Complexity Analysis:
- Time: O(N^2)
- Space: O(N)

Runtime: 2994 ms, faster than 5.23% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 77.9 MB, less than 5.23% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
"""
class Solution:
    mapper = {
            "a": 0, "e": 1, "i": 2, "o": 3, "u": 4
        }
    def check(self, s,  pre, l, r) -> bool:
        for i in range(5):
            if s[l] in self.mapper and i == self.mapper[s[l]]: cnt = 1
            else: cnt = 0
            if (pre[r][i] + pre[l][i] + cnt) % 2 != 0: return False
        return True
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        pre = [[0] * 5 for _ in range(n)]
        for i in range(n):
            for j in range(5):
                if s[i] in self.mapper and self.mapper[s[i]] == j:
                    pre[i][j] = pre[i-1][j] + 1
                else:
                    pre[i][j] = pre[i-1][j]
        for i in range(n-1, -1, -1):
            for j in range(n-i):
                if self.check(s, pre, j, i+j):
                    return i + 1
        return 0



"""
Solution II: prefix sum and bitmask dp

Complexity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 472 ms, faster than 59.74% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
Memory Usage: 19.8 MB, less than 51.95% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mapper = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        seen = {0: -1}
        res = cur = 0
        for i in range(len(s)):
            if s[i] in mapper:
                cur ^= mapper.get(s[i])
            if cur in seen:
                res = max(res, i - seen.get(cur))
            else:
                seen[cur] = i
        return res