# Problem Link: https://leetcode.com/problems/minimum-size-subarray-sum/



"""
Solution I: sliding window

Complexity Analysis:
- Time: O(N) where N denotes the length of the input list
- Space: O(1) for only integer variables created

Runtime: 76 ms, faster than 57.45% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 16.6 MB, less than 75.48% of Python3 online submissions for Minimum Size Subarray Sum.
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = total = 0
        ans = len(nums) + 1
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if ans == len(nums) + 1 else ans