# 3. Longest Substring Without Repeating Characters
# Medium
#
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Example 4:
# Input: s = ""
# Output: 0
#
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.



"""
Solution I:

Runtime: 40 ms, faster than 99.70% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.4 MB, less than 25.63% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = result = 0
        usedChar = {}
        for i, sub in enumerate(s):
            if sub in usedChar and start <= usedChar[sub]:
                start = usedChar[sub] + 1
            else:
                result = max(result, i-start+1)
            usedChar[sub] = i
        return result



"""
Solution II: sliding window

Complexity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 68 ms, faster than 57.45% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB, less than 24.98% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, ans = 0, 0
        counter = defaultdict(lambda: 0)
        for r in range(len(s)):
            while counter.get(s[r], 0) != 0:
                counter[s[l]] = counter.get(s[l], 0) - 1
                l += 1
            counter[s[r]] += 1
            ans = max(ans, r - l + 1)
        return ans