Problem Link: https://leetcode.com/problems/merge-intervals/

## Solution I
sorting then merge overlapping intervals

```python
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

# slightly revised
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表為空，或者當前區間與上一區間不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否則的話，我們就可以與上一區間進行合併
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
```

#### Complexity Analysis:
- Time: $O(NlogN)$ when it comes to sorting
- Space: $O(1)$ for using original list space