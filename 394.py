# Problem Link: https://leetcode.com/problems/decode-string/


# Solution I: Initial idea (wrong, but close to recursion)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        for char in s:
            if char == ']':
                tmp = ''
                while True:
                    i = stack.pop()
                    if i == '[':
                        break
                    else:
                        tmp += i
                tmp = tmp[::-1]
                # tmp = tmp * int(stack.pop())
                res += tmp
            else:
                stack.append(char)
        for i in stack:
            res += i
        return res


# Solution II: Stack
# Runtime: 32 ms, faster than 67.38% of Python3 online submissions for Decode String.
# Memory Usage: 14.2 MB, less than 51.75% of Python3 online submissions for Decode String.
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], '', 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = '', 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c) # 因為數字是一個一個讀進來的，所以要乘以10
            else:
                res += c
        return res


# Solution III: Recursion
# Runtime: 47 ms, faster than 19.60% of Python3 online submissions for Decode String.
# Memory Usage: 14.3 MB, less than 19.93% of Python3 online submissions for Decode String.
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = '', 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    tmp, i = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return res, i
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s, 0)