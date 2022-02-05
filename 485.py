# 485. Max Consecutive Ones
# Easy
#
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
#
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
#
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.



# Runtime: 332 ms, faster than 97.15% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.5 MB, less than 19.20% of Python3 online submissions for Max Consecutive Ones.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = tmpLength = 0
        for n in nums:
            if n:
                tmpLength += 1
            else:
                if tmpLength > maxLength:
                    maxLength = tmpLength
                tmpLength = 0
        return maxLength if maxLength > tmpLength else tmpLength



# Runtime: 340 ms, faster than 88.42% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.3 MB, less than 75.97% of Python3 online submissions for Max Consecutive Ones.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = tmpLength = 0
        for i, n in enumerate(nums):
            if n:
                tmpLength += 1
            else:
                if maxLength == 0 or tmpLength > maxLength:
                    maxLength = tmpLength
                tmpLength = 0
        if tmpLength > maxLength:
            maxLength = tmpLength
        return maxLength



# Runtime: 320 ms, faster than 99.90% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.4 MB, less than 49.21% of Python3 online submissions for Max Consecutive Ones.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m_substr = 0
        for k, v in groupby(nums):
            if k == 0:
                continue
                
            n = len(list(v))
            if n > m_substr:
                m_substr = n
        
        return m_substr



# Runtime: 344 ms, faster than 80.82% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.4 MB, less than 49.21% of Python3 online submissions for Max Consecutive Ones.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = tmpLength = 0
        for i, n in enumerate(nums):
            if n:
                tmpLength += 1
                if maxLength == 0 or tmpLength > maxLength:
                    maxLength = tmpLength
            else:
                tmpLength = 0
        return maxLength



# Runtime: 364 ms, faster than 43.80% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.3 MB, less than 75.97% of Python3 online submissions for Max Consecutive Ones.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxLength = tmpLength = 0
        for i, n in enumerate(nums):
            if n:
                tmpLength += 1
                maxLength = max(maxLength, tmpLength)
            else:
                tmpLength = 0
        return maxLength