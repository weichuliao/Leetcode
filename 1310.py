# Problem Link: https://leetcode.com/problems/xor-queries-of-a-subarray/



"""
Solution I: prefix sum

Complexity Analysis:
- Time: O(M+N) where M denotes the length arr and N denotes the length of queries
- Space: O(M+N) (M for pre and N for res)

Runtime: 540 ms, faster than 25.56% of Python3 online submissions for XOR Queries of a Subarray.
Memory Usage: 29.2 MB, less than 67.26% of Python3 online submissions for XOR Queries of a Subarray.
"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        res = []
        for i in range(len(arr)):
            pre.append(pre[i] ^ arr[i])
        for l, r in queries:
            res.append(pre[l] ^ pre[r+1])
        return res