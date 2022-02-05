# Problem Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/



"""
Solution I: sliding window with hash map

Complexity Analysis:
- Time: O(S+P) where S denotes the length of string s and P the length of string p
- Space: O(1) because p_count and s_count contain no more than 26 elements. 

Runtime: 144 ms, faster than 58.37% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15.4 MB, less than 10.59% of Python3 online submissions for Find All Anagrams in a String.
"""
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np: return []
        p_count = Counter(p)
        s_count = Counter()
        ans = []
        for r in range(ns):
            s_count[s[r]] += 1
            if r >= np:
                if s_count[s[r-np]] == 1: del s_count[s[r-np]]
                else: s_count[s[r-np]] -= 1
            if s_count == p_count: ans.append(r - np + 1)
        return ans



"""
Solution II: sliding window with list

Complexity Analysis:
- Time: O(S*P)
- Space: O(S*P)

Runtime: 150 ms, faster than 53.01% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15 MB, less than 93.65% of Python3 online submissions for Find All Anagrams in a String.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p: return []
        res, ns, np, p_count, s_count = [], len(s), len(p), [0]*26, [0]*26
        
        for c in p: p_count[ord(c)-ord('a')] += 1
            
        i = 0
        while i < ns and i < np:
            s_count[ord(s[i]) - ord('a')] += 1
            i += 1
            
        i, j = 0, np
        while i < ns - np + 1:
            if p_count == s_count: res.append(i)
            if j < ns: s_count[ord(s[j]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] -= 1
            i += 1
            j += 1
            
        return res
"""
slightly revised as below:

Runtime: 139 ms, faster than 61.14% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15.4 MB, less than 10.59% of Python3 online submissions for Find All Anagrams in a String.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        
        res, ns, np, p_count, s_count = [], len(s), len(p), [0]*26, [0]*26
        
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1        
        s_count[ord(s[len(p) -1]) - ord('a')] -= 1
            
        l = 0
        for r in range(len(p) - 1, len(s)):
            s_count[ord(s[r]) - ord('a')] += 1
            if(s_count == p_count):
                res.append(l)
            s_count[ord(s[l]) - ord('a')] -= 1
            l += 1

        return res