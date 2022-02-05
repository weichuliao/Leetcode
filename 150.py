# Problem Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/


"""
Solution I: Initial idea
Stack (do calculation when meeting operands and put results back to stack)

Complexity Analysis:
- Time: O(N) where N denotes the length of input list
- Space: O(N) for maintaining a stack to store the calculation process

Runtime: 60 ms, faster than 96.06% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14.5 MB, less than 69.62% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(int(i))
            else:
                if i == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                elif i == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif i == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                elif i == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
        return stack[0]