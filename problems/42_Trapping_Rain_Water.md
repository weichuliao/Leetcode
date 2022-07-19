Problem Link: https://leetcode.com/problems/trapping-rain-water/

## Solution I
dynamic programming

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        maxLeft = [0] * length
        maxRight = [0] * length
        minLR = [0] * length
        water = 0
        
        maxB = height[0]
        for i in range(length):
            maxLeft[i] = maxB
            if maxB < height[i]: maxB = height[i]
        
        maxB = height[-1]
        for i in range(length - 1, -1, -1):
            maxRight[i] = maxB
            if maxB < height[i]: maxB = height[i]
        
        for i in range(length):
            minLR[i] = min(maxLeft[i], maxRight[i])
        
        for i in range(length):
            temp = minLR[i] - height[i]
            water += temp if temp > 0 else 0
        
        return water
```

#### Complexity Analysis:
- Time: $O(N)$
- Space: $O(N)$

<br>

## Solution II
two pointers

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        ans = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                ans += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                ans += rightMax - height[right]

        return ans
```

#### Complexity Analysis:
- Time: $O(N)$
- Space: $O(1)$

<br>

## Solution III
monotonic stack

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        ans, cur = 0, 0
        stack = []
        while cur < len(height):
            while stack and height[cur] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if not stack: break
                distance = cur - stack[-1] - 1
                boundedHeight = min(height[cur], height[stack[-1]]) - height[top]
                ans += distance * boundedHeight
            stack.append(cur)
            cur += 1
        return ans
```

#### Complexity Analysis:
- Time: $O(N)$
- Space: $O(N)$