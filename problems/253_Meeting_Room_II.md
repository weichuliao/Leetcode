Problem Link: https://leetcode.com/problems/meeting-rooms-ii/

## Solution I
min heap, priority queue

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        free_rooms = []
        intervals.sort(key = lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)
```

#### Complexity Analysis:
- Time: $O(NlogN)$ for 1) sorting and 2) N extract-min operations and each operation takes O(logN).
- Space: $O(N)$ for a min heap containing N elements in worst case.

<br>

## Solution II
chronological ordering

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
```

#### Complexity Analysis:
- Time: $O(NlogN)$
- Space: $O(N)$