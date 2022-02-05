# Problem Link: https://leetcode.com/problems/replace-the-substring-for-balanced-string/



"""
Solution I: sliding window

Complexity Analysis:
- Time: O(N), one pass for counting, one pass for sliding window
- Space: O(1)

Runtime: 623 ms, faster than 12.85% of Python3 online submissions for Replace the Substring for Balanced String.
Memory Usage: 14.9 MB, less than 10.84% of Python3 online submissions for Replace the Substring for Balanced String.
"""
class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        res = n = len(s)
        left = 0
        for right, c in enumerate(s):
            count[c] -= 1
            while left < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1
        return res