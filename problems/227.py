# Problem Link: https://leetcode.com/problems/basic-calculator-ii/
# Reference Link: https://mp.weixin.qq.com/s?__biz=MzI4MzUxNjI3OA==&mid=2247486874&idx=2&sn=3f42546c132983bf22828a99b1c6e7b4&chksm=eb88c183dcff48956d97d1b67e8d070b9561be26f66006773d153457494ca8c43db73a8e7343&token=1469603194&lang=zh_CN#rd



"""
Solution I:

Compelxity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 64 ms, faster than 97.81% of Python3 online submissions for Basic Calculator II.
Memory Usage: 16.1 MB, less than 25.81% of Python3 online submissions for Basic Calculator II.
"""
class Solution:
    def calculate(self, s: str) -> int:
        stack, preflag, num = [], '+', 0
        s += '$'
        
        for c in s:
            if c.isdigit(): num = num * 10 + int(c)
            elif c == ' ': continue
            else:
                if preflag == '+': stack.append(num)
                elif preflag == '-': stack.append(-num)
                elif preflag == '*': stack.append(stack.pop() * num)
                elif preflag == '/': stack.append(int(stack.pop() / num))
                preflag, num = c, 0
        return sum(stack)