# Problem Link: https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/



"""
Solution I: prefix sum

Complexity Analysis:
- Time: O(N+N+N)
- Space: O(N)

Runtime: 547 ms, faster than 5.26% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
Memory Usage: 26 MB, less than 54.80% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
"""
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        l = [arr[0]] * n
        r = [arr[n-1]] * n
        res = arr[0]
        for i in range(1, n):
            l[i] = max(l[i-1] + arr[i], arr[i])
            res = max(res, l[i])
        for i in range(n - 2, -1, -1):
            r[i] = max(r[i+1] + arr[i], arr[i])
            res = max(res, r[i])
        for i in range(1, n - 1):
            res = max(res, l[i-1] + r[i+1])
        return res



"""
Solution II: dynamic programming

Complexity Analysis:
- Time: 
- Space: 


"""
