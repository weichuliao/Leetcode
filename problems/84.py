# Problem Link: https://leetcode.com/problems/largest-rectangle-in-histogram
# Explanation: https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode-/



# Solution: Monotonic stack
#
# Complexity Analysis
# Time: O(n) where n numbers are pushed and popped.
# Space: O(n. Stack is used.
#
# Runtime: 780 ms, faster than 76.55% of Python3 online submissions for Largest Rectangle in Histogram.
# Memory Usage: 28 MB, less than 35.10% of Python3 online submissions for Largest Rectangle in Histogram.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [-1]
        for idx, val in enumerate(heights):
            while stack[-1] != -1 and val <= heights[stack[-1]]:
                curr_height = heights[stack.pop()]
                curr_width = idx - stack[-1] - 1
                ans = max(ans, curr_height * curr_width)
            stack.append(idx)
            
        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1] - 1
            ans = max(ans, curr_height * curr_width)
            
        return ans