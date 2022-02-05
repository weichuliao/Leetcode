# Problem Link: 



"""
Solution I: sorting then merge overlapping intervals

Complexity Analysis:
- Time: O(NlogN) when it comes to sorting
- Space: O(1) for using original list space

Runtime: 238 ms, faster than 5.02% of Python3 online submissions for Merge Intervals.
Memory Usage: 18 MB, less than 12.15% of Python3 online submissions for Merge Intervals.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda a: a[0])
        i = 0
        while i < len(intervals) - 1:
            current = intervals[i]
            next = intervals[i+1]
            if current[0] > next[1] or current[1] < next[0]:
                pass
            else:
                intervals[i] = None
                intervals[i+1] = [min(current[0], next[0]), max(current[1], next[1])]
            i += 1
        return list(filter(lambda x: x, intervals))
"""
slight revised as below:

Runtime: 144 ms, faster than 8.61% of Python3 online submissions for Merge Intervals.
Memory Usage: 18.2 MB, less than 12.15% of Python3 online submissions for Merge Intervals.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged