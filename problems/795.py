# Problem Link: 



"""
Solution I: prefix sum

Complexity Analysis:
- Time: O(N) where N denotes the length of nums
- Space: O(1)

Runtime: 929 ms, faster than 6.48% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
Memory Usage: 22.2 MB, less than 78.84% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
"""
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def notGreater(bound):
            ans = counter = 0
            for num in nums:
                if num <= bound: counter += 1
                else: counter = 0
                ans += counter
            return ans
        return notGreater(right) - notGreater(left - 1)