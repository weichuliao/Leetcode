# 1512. Number of Good Pairs
# Easy
#
# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.
#
# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#
# Example 3:
# Input: nums = [1,2,3]
# Output: 0
#
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#
# Hint:
# Count how many times each number appears. If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.


# Solution I:
# Runtime: 20 ms, faster than 99.62% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 14 MB, less than 90.79% of Python3 online submissions for Number of Good Pairs.
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = [0] * 100
        for num in nums:
            count[num-1] += 1
        result = 0
        for i in count:
            if i > 0:
                result += i * (i-1) // 2
        return result