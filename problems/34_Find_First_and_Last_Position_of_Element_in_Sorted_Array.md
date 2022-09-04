Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Solution I
two binary searches

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_leftmost():
            left = 0
            right = len(nums) - 1
            left_most = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    left_most = mid
                    right = mid - 1
            return left_most
        
        def find_rightmost():
            left = 0
            right = len(nums) - 1
            right_most = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right_most = mid
                    left = mid + 1
            return right_most
        
        left = find_leftmost()
        if left == -1: return [-1, -1]
        right = find_rightmost()
        return [left, right]
```

#### Complexity Analysis:
- Time: $O(logN)$
- Space: $O(1)$