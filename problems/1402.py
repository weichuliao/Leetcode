# Problem Link: https://leetcode.com/problems/reducing-dishes/



"""
Solution I: prefix sum / greedy

Complexity Analysis:
- Time: O(NlogN) dominated by sorting
- Space: O(logN) 使用语言自带的排序，空间复杂度为 O(logN)。如果使用堆排序，空间复杂度可以降低至 O(1)

Runtime: 40 ms, faster than 81.72% of Python3 online submissions for Reducing Dishes.
Memory Usage: 14.3 MB, less than 50.51% of Python3 online submissions for Reducing Dishes.
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        presum = ans = 0
        for si in satisfaction:
            if presum + si > 0:
                presum += si
                ans += presum
            else:
                break
        return ans