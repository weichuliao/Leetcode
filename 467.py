# Problem Link: https://leetcode.com/problems/unique-substrings-in-wraparound-string/



"""
Solution I: prefix sum

Complexity Analysis:
- Time: O(N) where N denotes the length of string p
- Space: 由于最多存储 26 个字母， 因此空间实际上是常数，故空间复杂度为 O(1)

Runtime: 123 ms, faster than 24.22% of Python3 online submissions for Unique Substrings in Wraparound String.
Memory Usage: 14.4 MB, less than 55.90% of Python3 online submissions for Unique Substrings in Wraparound String.
"""
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p = '^' + p
        w = 1
        len_mapper = collections.defaultdict(lambda: 0)
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i]) - ord(p[i-1]) == -25:
                w += 1
            else:
                w = 1
            len_mapper[p[i]] = max(len_mapper[p[i]], w)
        return sum(len_mapper.values())