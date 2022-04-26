from collections import Counter
from math import floor

class Solution:
    def solution(self, s: str, t: str) -> int:
        scount = Counter(s)
        tcount = Counter(t)
        ans = float('inf')
        for c in tcount:
            ans = min(ans, floor(scount[c] / tcount[c]))
        return ans

execution = Solution()
result = execution.solution('abcabcabacbacbababcbabc', 'bca')
print('The answer is', result)