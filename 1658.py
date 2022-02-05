# Problem Link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/



"""
Solution I: 

Complexity Analysis:
- Time: O(N) where N is the length of nums
- Space: O(1)

Runtime: 1124 ms, faster than 92.73% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
Memory Usage: 28.6 MB, less than 47.97% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        target = sum(nums) - x
        window = 0
        ans = len(nums)
        if target == 0: return ans
        for right in range(len(nums)):
            window += nums[right]
            while left < right and window > target:
                window -= nums[left]
                left += 1
            if window == target:
                ans = min(ans, len(nums) - (right - left + 1))
        return -1 if ans == len(nums) else ans