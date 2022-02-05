# Problem Link: 

# Solution I: Intuition - use slow and fast pointers to track temperatures
# Time Limit Exceeded
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        slow = 0
        fast = slow + 1
        ans = []
        while fast < len(temperatures):
            if temperatures[fast] > temperatures[slow]:
                ans.append(fast - slow)
                slow += 1
                fast = slow + 1
            else:
                if fast == len(temperatures) - 1:
                    ans.append(0)
                    slow += 1
                    fast = slow + 1
                else:
                    fast += 1
        ans.append(0)
        return ans



# Solution II: Monotonic stack
# maintaining a decreasing-ordered stack of temperatures by popping out the elements in stack
# at the same time (when popping out the elements in stack), calculate the days
# Complexity Analysis:
# Time: Since the elements of input are only appended and popped at motst one time,
#       the time complexity is O(N) where N denotes the length of input
# Space: Since stack is used and its size is the same as that of the input list,
#        the space complexity is O(N) where N denotes the length of input list
#
# Runtime: 1184 ms, faster than 93.06% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 25.2 MB, less than 68.65% of Python3 online submissions for Daily Temperatures.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return ans