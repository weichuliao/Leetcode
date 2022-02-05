# Problem Link: https://leetcode.com/problems/basic-calculator/



"""
Solution I:

Complexity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 113 ms, faster than 41.28% of Python3 online submissions for Basic Calculator.
Memory Usage: 16.1 MB, less than 20.40% of Python3 online submissions for Basic Calculator.
"""
class Solution:
    def calculate(self, s: str) -> int:
        def dfs(s, start):
            stack, preflag, num, i = [], '+', 0, start
            while i < len(s):
                c = s[i]
                if c == ' ':
                    i += 1
                    continue
                elif c == '(': i, num = dfs(s, i+1)
                elif c.isdigit(): num = num * 10 + int(c)
                else:
                    if preflag == '+': stack.append(num)
                    elif preflag == '-': stack.append(-num)
                    if c == ')': break
                    preflag, num = c, 0
                i += 1
            return i, sum(stack)
        s += '$'
        return dfs(s, 0)[1]