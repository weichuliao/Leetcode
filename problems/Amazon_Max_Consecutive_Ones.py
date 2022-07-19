# Link: https://leetcode.com/discuss/interview-question/algorithms/125017/amazon-max-consecutive-ones/125014

'''
Given a binary array and an integer m, find the position of zeroes flipping which creates maximum number of consecutive 1s in array.

Example 1:

Input: arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], m = 2
Output: [5, 7]
Explanation:
We are allowed to flip maximum 2 zeroes. If we flip arr[5] and arr[7], we get 8 consecutive 1's which is
maximum possible under given constraints 

Example 2:

Input: arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], m = 1
Output: [7]

Example 3:

Input: arr = [0, 0, 0, 1], m = 4
Output: [0, 1, 2]
'''

from typing import List
from collections import deque

class Solution:
    def maxConsecutiveOnes(self, nums: List[int], k: int) -> List[int]:
        left = 0
        ans = deque()
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
                ans.append(right)
            while k < 0:
                if nums[left] == 0:
                    k += 1
                    ans.popleft()
                left += 1
        return ans

execution = Solution()
result = execution.maxConsecutiveOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
print('The answer is', result)
result = execution.maxConsecutiveOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1] , 3)
print('The answer is', result)
result = execution.maxConsecutiveOnes([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 2)
print('The answer is', result)
result = execution.maxConsecutiveOnes([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 1)
print('The answer is', result)
result = execution.maxConsecutiveOnes([0, 0, 0, 1], 4)
print('The answer is', result)