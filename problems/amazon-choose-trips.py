from typing import List

class Solution:
    def chooseTrips(self, weights: List[int]) -> int:
        counter = dict()
        for w in weights:
            if w in counter:
                counter[w] += 1
            else:
                counter[w] = 1
        ans = 0
        for key in counter:
            if counter[key] % 3 == 0:
                ans += counter[key] // 3
            elif counter[key] % 2 == 0:
                ans += counter[key] // 2
            else:
                return -1
        return ans

execution = Solution()
assert execution.chooseTrips([1, 3, 4, 4, 3, 1, 1]) == 3
assert execution.chooseTrips([10, 10, 8, 8, 8, 8, 5]) == -1