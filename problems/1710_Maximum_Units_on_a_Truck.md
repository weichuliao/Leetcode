Problem Link: https://leetcode.com/problems/maximum-units-on-a-truck/

## Solution I
sorting

```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box = sorted(boxTypes, key=lambda x: (-x[1], x[0]))
        res = counter = 0
        for num, unit in sorted_box:
            for i in range(num):
                res += unit
                counter += 1
                # truck is fully filled
                if counter == truckSize:
                    return res
        # truck is not fully filled
        return res

# another version
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box = sorted(boxTypes, key=lambda x: -x[1])
        res = 0
        for num, unit in sorted_box:
            count = min(truckSize, num)
            res += count * unit
            truckSize -= count
            if truckSize == 0:
                break
        return res
```

#### Complexity Analysis:
- Time: $O(nlogn)$ for sorting dominating the time; $O(nlogn)+O(n)=O(nlogn)$.
- Space: $O(1)$

<br>

## Solution II
heap (priority queue)

```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxHeap = list((-unit, num) for num, unit in boxTypes)
        heapq.heapify(boxHeap)
        res = 0
        while boxHeap:
            unit, num = heapq.heappop(boxHeap)
            boxCount = min(truckSize, num)
            res += boxCount * -unit
            truckSize -= boxCount
            if truckSize == 0: break
        return res
```

#### Complexity Analysis:
- Time: $O(nlogn)$
  - $O(n)$: adding all the elements in priority queue.
  - $O(nlogn)$: iterating through priority queue takes `n` times and deleting elements from priority queue takes $O(logn)$ time.
- Space: $O(n)$ as we use a queue of size `n`.