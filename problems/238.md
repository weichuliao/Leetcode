Problem Link: https://leetcode.com/problems/product-of-array-except-self/

## Solution I
two prefix product lists

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right = [0] * length, [0] * length
        
        left[0] = 1
        for i in range(length - 1):
            left[i+1] = nums[i] * left[i]
        
        right[length - 1] = 1
        for i in range(length - 1, 0, -1):
            right[i-1] = nums[i] * right[i]
        
        ans = []
        for i in range(length):
            ans.append(left[i] * right[i])
        
        return ans
```

#### Complexity Analysis:
- Time: $O(n)$
- Space: $O(n)$

---

## Solution II
prefix product

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length
        
        ans[0] = 1
        for i in range(length - 1):
            ans[i+1] = nums[i] * ans[i]
        
        right = 1
        for i in range(length - 1, -1, -1):
            ans[i] = right * ans[i]
            right *= nums[i]
        
        return ans
```

#### Complexity Analysis:
- Time: $O(n)$
- Space: $O(1)$