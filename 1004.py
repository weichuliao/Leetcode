# Problem Link: https://leetcode.com/problems/max-consecutive-ones-iii/



"""
Solution I: sliding window

Complexity Analysis:
- Time: O(N), where N is the number of elements in the array. In worst case we might end up visiting every element of array twice, once by left pointer and once by right pointer.
- Space: O(1). We do not use any extra space.

Runtime: 959 ms, faster than 17.96% of Python3 online submissions for Max Consecutive Ones III.
Memory Usage: 14.9 MB, less than 35.95% of Python3 online submissions for Max Consecutive Ones III.
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1
"""
Complexity Analysis:
- Time: O(N)
- Space: O(1)

Runtime: 1040 ms, faster than 12.51% of Python3 online submissions for Max Consecutive Ones III.
Memory Usage: 14.8 MB, less than 35.95% of Python3 online submissions for Max Consecutive Ones III.
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = ans = 0
        for right in range(len(nums)):
            k -= nums[right] == 0
            while k < 0:
                k += nums[left] == 0
                left += 1
            ans = max(ans, right - left + 1)
        return ans
"""
slightly revised as below

Runtime: 987 ms, faster than 15.72% of Python3 online submissions for Max Consecutive Ones III.
Memory Usage: 14.9 MB, less than 35.95% of Python3 online submissions for Max Consecutive Ones III.
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1