# Problem Link: https://leetcode.com/problems/corporate-flight-bookings/



"""
Solution I: prefix sum

Complexity Analysis:
- Time: O(N) where N denotes the legnth of list
- Space: O(N)

Runtime: 868 ms, faster than 59.30% of Python3 online submissions for Corporate Flight Bookings.
Memory Usage: 28.4 MB, less than 28.35% of Python3 online submissions for Corporate Flight Bookings.
"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        counter = [0] * (n + 1)
        for i, j, k in bookings:
            counter[i-1] += k
            if j < n: counter[j] -= k
        for i in range(n + 1):
            counter[i] += counter[i-1]
        return counter[:-1]