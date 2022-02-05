# Problem Link: https://leetcode.com/problems/insert-interval/



"""
Solution I: sorting - add newInterval into intervals and sort

Complexity Analysis:
- Time: O(NlogN) when it comes to sorting
- Space: O(1) for not creating new variables

Runtime: 108 ms, faster than 16.20% of Python3 online submissions for Insert Interval.
Memory Usage: 17.5 MB, less than 92.22% of Python3 online submissions for Insert Interval.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda a: a[0])
        
        def intersected(a, b):
            if a[0] > b[1] or a[1] < b[0]:
                return False
            return True
        
        def mergeTwo(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]
        
        i = 0
        while i < len(intervals) - 1:
            current = intervals[i]
            next = intervals[i+1]
            if intersected(current, next):
                intervals[i] = None
                intervals[i+1] = mergeTwo(current, next)
            i += 1
            
        return list(filter(lambda x: x, intervals))



"""
Solution II: scanning once

Complexity Analysis:
- Time: O(N)
- Space: O(1)

Runtime: 88 ms, faster than 28.38% of Python3 online submissions for Insert Interval.
Memory Usage: 17.6 MB, less than 32.17% of Python3 online submissions for Insert Interval.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def intersected(a, b):
            if a[0] > b[1] or a[1] < b[0]: return False
            return True
            
        i, n = 0, len(intervals)
        ans = []
        # 前
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        # 中
        while i < n and intersected(intervals[i], newInterval):
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        ans.append(newInterval)
        # 後
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans