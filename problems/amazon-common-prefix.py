# Link: https://leetcode.com/discuss/interview-question/851513/roblox-new-grad-2021-oa-hackerrank
# Sol Ref: https://www.geeksforgeeks.org/sub-strings-of-a-string-that-are-prefix-of-the-same-string/
# Algo Ref: https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm

from typing import List

class Solution:
    def commonPrefixLength(self, input: str) -> int:
        n = len(input)
        z = [0] * n
        l = r = 0

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and input[z[i]] == input[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        return n + sum(z)

execution = Solution()
result = execution.commonPrefixLength('abcabcd')
print('The answer is', result)
assert execution.commonPrefixLength("abcabcd") == 10
assert execution.commonPrefixLength("ababaa") == 11
assert execution.commonPrefixLength("aa") == 3
