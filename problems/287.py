# Problem Link: https://leetcode.com/problems/find-the-duplicate-number/
# similar question: #41



"""
Solution I: negative marking

Complexity Analysis:
- Time: O(n)
- Space: O(1)

Runtime: 814 ms, faster than 52.89% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 28 MB, less than 89.48% of Python3 online submissions for Find the Duplicate Number.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]
        # restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return duplicate



"""
Solution II: array as hash map (iterative)

Complexity Ananlysis:
- Time: O(n)
- Space: O(1)

Runtime: 664 ms, faster than 68.78% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 27.9 MB, less than 89.48% of Python3 online submissions for Find the Duplicate Number.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]



"""
Solution III: binary search
"""




"""
Solution IV: sum of set bits
"""




"""
Solution V: cycle detection (two pointers)

Complexity Ananlysis:
- Time: O(n)
- Space: O(1)

Runtime: 720 ms, faster than 60.52% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 27.9 MB, less than 89.48% of Python3 online submissions for Find the Duplicate Number.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare