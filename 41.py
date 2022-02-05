# Problem Link: https://leetcode.com/problems/first-missing-positive/
# Explanation: https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/

"""
Solution I: cycle sort?

Complexity Analysis:
- Time: O(N+N) in worst case, where N denotes the length of input list
- Space: O(N) where N denotes the length of input list, no other large data structure created

Runtime: 936 ms, faster than 51.49% of Python3 online submissions for First Missing Positive.
Memory Usage: 60.3 MB, less than 62.93% of Python3 online submissions for First Missing Positive.
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 
        i = 0
        while i < len(nums):
            num = nums[i] # curr val
            if 0 < nums[i] <= len(nums) and nums[i] != nums[num-1]:
                nums[i], nums[num-1] = nums[num-1], nums[i]
            else: i += 1

        # 
        for i in range(len(nums)):
            if i+1 != nums[i]: return i+1

        return nums[-1] + 1