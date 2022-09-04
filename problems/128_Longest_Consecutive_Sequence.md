Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/

## Solution I

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        
        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
```

#### Complexity Analysis:
- Time: $O(N)$. The while loop is reached only when `current_num` marks the beginning of a sequence (i.e. `current_num - 1` is not present in nums). The while loop can only run for `n` iterations throughout the entire runtime of the algorithm. This means that the nested loops actually run in $O(N + N) = O(N)$ time.
- Space: $O(N)$