Problem Link: https://leetcode.com/problems/subsets/



## Solution I
backtracking

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.track = []
        self.backtrack(nums, 0, self.track)
        return self.res
    def backtrack(self, nums, start, track):
        self.res.append(list(self.track))
        for i in range(start, len(nums)):
            self.track.append(nums[i])
            self.backtrack(nums, i+1, self.track)
            self.track.pop()
```

#### Complexity Analysis:
- Time:
- Space:

---

## Solution II
another backtracking solution

```python
# another version
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
```

#### Complexity Analysis:
- Time: $O(n * 2^n)$
- Space: $O(2^n)$