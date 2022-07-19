from typing import List

class Solution:
    def getNonInclusiveRetailor(self, intervals: List[List[int]]) -> int:
        # sort the intervals by starting time
        intervals.sort(key = lambda x: x[0])

        # iterate through the list to eliminate overlapping intervals
        ans = 0
        last_end = intervals[0][1]
        for index, interval in enumerate(intervals):
            if index == 0: continue
            if last_end <= interval[0]:
                last_end = max(last_end, interval[1])
            else:
                ans += 1
        return ans

execution = Solution()
result = execution.getNonInclusiveRetailor([[1, 2], [2, 3], [3, 5], [4, 5]])
print('The answer is', result)
result = execution.getNonInclusiveRetailor([[1, 5], [2, 3], [3, 5], [4, 5]])
print('The answer is', result)
result = execution.getNonInclusiveRetailor([[1, 5], [2, 3], [3, 5], [1, 7], [4, 5], [1, 6]])
print('The answer is', result)