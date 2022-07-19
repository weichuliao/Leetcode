Problem Link: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

## Solution I

```python
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        res = 0
        n = len(s)
        left, right = [0] * n, [0] * n

        pos = {}
        for idx, char in enumerate(s):
            if char in pos:
                left[idx] = pos[char]
            else:
                left[idx] = -1
            pos[char] = idx

        pos = {}
        for idx in range(n - 1, -1, -1):
            char = s[idx]
            if char in pos:
                right[idx] = pos[char]
            else:
                right[idx] = n
            pos[char] = idx

        for idx in range(n):
            res += (idx - left[idx]) * (right[idx] - idx)

        return res
```

#### Complexity Analysis:
- Time: $O(N)$
- Space: $O(N)$