# Problem Link: https://leetcode.com/problems/add-to-array-form-of-integer/

"""
Solution I: intuition - simulation of the process

Complexity Analysis:
- Time: O(N+N) where N denotes the number of digits of the input and output list
- Space: O(N) for a new list was created to store digits of the ouput number

Runtime: 5100 ms, faster than 5.11% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15.3 MB, less than 30.82% of Python3 online submissions for Add to Array-Form of Integer.
"""
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res, n = 0, len(num)
        for i in range(n):
            res += num[i] * 10 ** (n-i-1)
        res += k
        
        ans = []
        while res > 0:
            ans.append(res % 10)
            res //= 10
        
        if len(ans) <= 0: return [0]
        return ans[::-1]



"""
Solution II: from submissions

Runtime: 284 ms, faster than 83.04% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15.1 MB, less than 54.98% of Python3 online submissions for Add to Array-Form of Integer.
"""
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return str(int(''.join(str(e) for e in num)) + k)