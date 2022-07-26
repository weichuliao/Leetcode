Problem Link: https://leetcode.com/problems/contains-duplicate/

## Solution I
brute force but TLE

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]: return True
        return False
```

#### Complexity Analysis:
- Time: $O(n^2)$
- Space: $O(1)$

---

## Solution II
sorting

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]: return True
        return False
```

#### Complexity Analysis:
- Time: $O(nlogn)$
- Space: $O(1)$

---

## Solution III
one pass with set

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
```

#### Complexity Analysis:
- Time: $O(n)$
- Space: $O(n)$