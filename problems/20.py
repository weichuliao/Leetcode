# Problem Link: https://leetcode.com/problems/valid-parentheses/



"""
Solution I: stack

Complexity Analysis:
- Time: O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack take O(1) time.
- Space: O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((.

Runtime: 28 ms, faster than 89.53% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.4 MB, less than 36.09% of Python3 online submissions for Valid Parentheses.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element: return False
            else: stack.append(char)
        return not stack