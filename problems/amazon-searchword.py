class Solution:
    def solution(self, search: str, result: str) -> int:
        ptrs = ptrr = 0
        ans = ''
        while ptrs < len(search) or ptrr < len(result):
            if ptrs >= len(search):
                break
            if ptrr >= len(result):
                break
            if search[ptrs] == result[ptrr]:
                ptrs += 1
                ptrr += 1
            else: ptrs += 1
        return abs((len(search) - ptrs) - (len(result) - ptrr))

execution = Solution()
result = execution.solution('armaze', 'amazon')
print('The answer is', result)
result = execution.solution('abc', 'cdhbqaab')
print('The answer is', result)
result = execution.solution('cdhbqaab', 'abc')
print('The answer is', result)