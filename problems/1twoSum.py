# 1. Two Sum
# Easy
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



# Solution I:
# Runtime: 60 ms, faster than 74.73% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 41.77% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []





# Solution II:
# Runtime: 68 ms, faster than 49.36% of Python3 online submissions for Two Sum.
# Memory Usage: 15.5 MB, less than 14.57% of Python3 online submissions for Two Sum.

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         new_nums = []
#         for idx, val in enumerate(nums):
#             new_nums.append([val, idx])
#         new_nums.sort()
        
#         left, right = 0, len(new_nums) - 1
#         while left < right:
#             sum = new_nums[left][0] + new_nums[right][0]
#             if sum > target:
#                 right -= 1
#             elif sum < target:
#                 left += 1
#             else:
#                 return [new_nums[left][1], new_nums[right][1]]
#         return []