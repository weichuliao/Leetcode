# Problem Link: https://leetcode.com/problems/longest-turbulent-subarray/



"""
Solution I: sliding window

Complexity Analysis:
- Time: O(N) where N is the length of arr
- Space: O(1)

Runtime: 844 ms, faster than 14.29% of Python3 online submissions for Longest Turbulent Subarray.
Memory Usage: 18 MB, less than 47.01% of Python3 online submissions for Longest Turbulent Subarray.
"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def cmp(a, b):
            return (a > b) - (a < b)
        
        n = len(arr)
        ans, anchor = 1, 0
        for i in range(1, n):
            c = cmp(arr[i-1], arr[i])
            if c == 0: anchor = i
            elif i == n - 1 or c * cmp(arr[i], arr[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans