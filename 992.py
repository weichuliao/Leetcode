# Problem Link: https://leetcode.com/problems/subarrays-with-k-different-integers/



"""
Solution I: prefix sum

Complexity Analysis:
- Time: O(N) where N denotes the length of fruits
- Space: O(k)

Runtime: 589 ms, faster than 48.30% of Python3 online submissions for Subarrays with K Different Integers.
Memory Usage: 17.6 MB, less than 14.42% of Python3 online submissions for Subarrays with K Different Integers.
"""
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            win = collections.Counter()
            l = ans = 0
            for r, num in enumerate(nums):
                if win[num] == 0: k -= 1
                win[num] += 1
                while k < 0:
                    win[nums[l]] -= 1
                    if win[nums[l]] == 0: k += 1
                    l += 1
                ans += r - l + 1
            return ans
        return atMostK(nums, k) - atMostK(nums, k - 1)



"""
Solution II: sliding window

Complexity Analysis:
- Time: O(n)，其中 n 是数组长度。我们至多只需要遍历该数组三次（右指针和两个左指针各一次）。
- Space: O(n)，其中 n 是数组长度。我们需要记录每一个数的出现次数，本题中数的大小不超过数组长度。

Runtime: 608 ms, faster than 41.97% of Python3 online submissions for Subarrays with K Different Integers.
Memory Usage: 17.5 MB, less than 29.19% of Python3 online submissions for Subarrays with K Different Integers.
"""
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num1, num2 = collections.Counter(), collections.Counter()
        tot1 = tot2 = left1 = left2 = right = ret = 0
        for right, num in enumerate(nums):
            if num1[num] == 0: tot1 += 1
            num1[num] += 1
            if num2[num] == 0: tot2 += 1
            num2[num] += 1
            while tot1 > k:
                num1[nums[left1]] -= 1
                if num1[nums[left1]] == 0: tot1 -= 1
                left1 += 1
            while tot2 > k - 1:
                num2[nums[left2]] -= 1
                if num2[nums[left2]] == 0: tot2 -= 1
                left2 += 1
            ret += left2 - left1
        return ret