Problem Link: https://leetcode.com/problems/generate-parentheses/

## Solution I
backtracking, recursion

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, result = [], []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return result
```

#### Complexity Analysis:
- Time: $O(4^n/n^(1/2))$. Each valid sequence has at most n steps during the backtracking procedure.
- Space: $O(4^n/n^(1/2))$ for stack, and $O(N)$ for storing the sequence.