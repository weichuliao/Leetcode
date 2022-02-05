# Problem Link: https://leetcode.com/problems/binary-subarrays-with-sum/



"""
Solution I: prefix sum

Complexity Analysis:
- Time: O(N) where N denotes the length of nums
- Space: O(N)

Runtime: 496 ms, faster than 9.71% of Python3 online submissions for Binary Subarrays With Sum.
Memory Usage: 18.9 MB, less than 5.45% of Python3 online submissions for Binary Subarrays With Sum.
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in prefix:
            ans += count[x]
            count[x + goal] += 1

        return ans



"""
Solution II: sliding window

Complexity Analysis:
- Time: O(N) where N denotes the length of nums
- Space: O(1)

Runtime: 390 ms, faster than 21.56% of Python3 online submissions for Binary Subarrays With Sum.
Memory Usage: 15 MB, less than 84.36% of Python3 online submissions for Binary Subarrays With Sum.
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMostK(nums, goal):
            if goal < 0: return 0
            i = res = 0
            for j in range(len(nums)):
                goal -= nums[j]
                while goal < 0:
                    goal += nums[i]
                    i += 1
                res += j - i + 1
            return res
        return atMostK(nums, goal) - atMostK(nums, goal - 1)