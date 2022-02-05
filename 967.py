# Problem Link: https://leetcode.com/problems/numbers-with-same-consecutive-differences/



"""
Solution I: dfs

Complexity Analysis:
- Time: O(2^N)
- Space: O(2^N)

Runtime: 32 ms, faster than 98.83% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 14.3 MB, less than 94.53% of Python3 online submissions for Numbers With Same Consecutive Differences.
"""
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        ans = []
        def dfs(n, num):
            if n == 0:
                return ans.append(num)
            tail_digit = num % 10
            next_digits = set([tail_digit + k, tail_digit - k])
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    dfs(n - 1, new_num)
        for num in range(1, 10):
            dfs(n - 1, num)
        return list(ans)



"""
Solution II: bfs

Complexity Analysis:
- Time: O(2^N)
- Space: O(2^N)

Runtime: 40 ms, faster than 83.20% of Python3 online submissions for Numbers With Same Consecutive Differences.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Numbers With Same Consecutive Differences.
"""
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        queue = [digit for digit in range(1, 10)]
        for level in range(n-1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                next_digits = set([tail_digit + k, tail_digit - k])
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)
            queue = next_queue
        return queue