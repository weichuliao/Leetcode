# Problem Link: https://leetcode.com/problems/missing-number/
# https://leetcode-cn.com/problems/missing-number/solution/que-shi-shu-zi-by-leetcode/


# Solution I:
# Runtime: 2416 ms, faster than 6.87% of Python3 online submissions for Missing Number.
# Memory Usage: 15.6 MB, less than 17.41% of Python3 online submissions for Missing Number.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i


# Solution II: Sorting
# Runtime: 181 ms, faster than 34.29% of Python3 online submissions for Missing Number.
# Memory Usage: 15.4 MB, less than 49.16% of Python3 online submissions for Missing Number.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        
        if nums[0] != 0:
            return 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                return nums[i-1] + 1


# Solution III: Sorting + Binary Search
# Runtime: 228 ms, faster than 22.02% of Python3 online submissions for Missing Number.
# Memory Usage: 15.4 MB, less than 49.16% of Python3 online submissions for Missing Number.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i


# Solution IV: Hash Table
# Runtime: 124 ms, faster than 92.61% of Python3 online submissions for Missing Number.
# Memory Usage: 15.8 MB, less than 10.06% of Python3 online submissions for Missing Number.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in num_set:
                return i


# Solution V: Bit Manipulation
# Solution VI: Math