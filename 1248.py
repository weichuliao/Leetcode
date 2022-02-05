# Problem Link: https://leetcode.com/problems/count-number-of-nice-subarrays/



"""
Solution I: sliding window

Complexity Analysis:
- Time: O(N)
- Space: O(1)

Runtime: 936 ms, faster than 55.70% of Python3 online submissions for Count Number of Nice Subarrays.
Memory Usage: 21.2 MB, less than 24.68% of Python3 online submissions for Count Number of Nice Subarrays.
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            left = ans = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1: k -= 1
                while k < 0:
                    if nums[left] % 2 == 1: k += 1
                    left += 1
                ans += right - left + 1
            return ans
        return atMostK(nums, k) - atMostK(nums, k - 1)