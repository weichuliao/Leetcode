# Problem Link: https://leetcode.com/problems/last-stone-weight/



"""
Solution I: heap-based simulation

Complexity Analysis:
- Time: O(NlogN)
- Space: O(N) or O(logN)

Runtime: 42 ms, faster than 35.19% of Python3 online submissions for Last Stone Weight.
Memory Usage: 14.2 MB, less than 81.34% of Python3 online submissions for Last Stone Weight.
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)
        return -heapq.heappop(stones) if stones else 0