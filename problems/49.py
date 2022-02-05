# Problem Link: https://leetcode.com/problems/group-anagrams/



"""
Solution I: bucket sort

Complexity Analysis:
- Time: O(N * M) where N is the length of strs and M is the average length of string in strs
- Space: O(N * M)

Runtime: 112 ms, faster than 56.88% of Python3 online submissions for Group Anagrams.
Memory Usage: 19.3 MB, less than 23.87% of Python3 online submissions for Group Anagrams.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = collections.defaultdict(list)
        for s in strs:
            s_key = [0] * 26
            for c in s:
                s_key[ord(c)-ord('a')] += 1
            str_dict[tuple(s_key)].append(s)
        return list(str_dict.values())