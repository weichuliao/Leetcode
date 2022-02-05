# Problem Link: https://leetcode.com/problems/shortest-distance-to-a-character/

"""
Solution I: traverse list and calculate the distance from left and right

Complexity Analysis:
- Time: O(N^2) where N denotes the length of input string, and we have two layers of for loop
- Space: O(N) for a list storing the answers, where N denotes the length of input string

Runtime: 68 ms, faster than 41.64% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14.4 MB, less than 59.82% of Python3 online submissions for Shortest Distance to a Character.
"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [0] * len(s)
        for i in range(len(s)):
            if s[i] == c: continue
            shortest = float('inf')
            for r in range(i, len(s)):
                if s[r] == c:
                    shortest = min(shortest, r - i)
                    break
            for l in range(i, -1, -1):
                if s[l] == c:
                    shortest = min(shortest, i - l)
                    break
            ans[i] = shortest
        return ans



"""
Solution II: record the indice of target character in N and traverse the string to calculate the distance using recorded indice

Complexity Analysis:
- Time: O(N*K) where N denotes the length of input string and K denotes the number of target character in N (K <= N)
- Space: O(N+K) where N used for storing the answers and K for storing the index of target character in N

Runtime: 64 ms, faster than 44.44% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14.2 MB, less than 95.74% of Python3 online submissions for Shortest Distance to a Character.
"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        cIndex, res = [], [float('inf')] * n
        
        for idx, char in enumerate(s):
            if char == c:
                cIndex.append(idx)
                res[idx] = 0
                
        for idx, char in enumerate(s):
            if s[idx] == c: continue
            for j in cIndex:
                dist = abs(j - idx)
                # break if new distance is larger than current distance stored = min()
                if dist > res[idx]: break
                res[idx] = dist
        
        return res



"""
Solution III: greedy

Complexity Analysis:
- Time: O(N + N) where N denotes the length of input string
- Space: O(N) for creating a list to store the answers

Runtime: 40 ms, faster than 78.98% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14.4 MB, less than 27.95% of Python3 online submissions for Shortest Distance to a Character.
"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [0 if s[i] == c else None for i in range(n)]
        
        for i in range(1, n):
            if res[i] != 0 and res[i-1] is not None:
                res[i] = res[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if res[i] is None or res[i+1] + 1 < res[i]:
                res[i] = res[i+1] + 1
        
        return res



"""
Solution IV: window

Complexity Analysis:
- Time: O(N + N) where N denotes the length of input string
- Space: O(N) for creating a list to store the answers

Runtime: 36 ms, faster than 93.07% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 14.4 MB, less than 27.95% of Python3 online submissions for Shortest Distance to a Character.
"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [0 for _ in range(n)]
        l = 0 if s[0] == c else n   # winodw left boundary
        r = s.find(c, 1)   # window right boundary
        
        for i in range(n):
            res[i] = min(abs(i-l), abs(r-i))
            # if approaching right boundary, change the window
            if i == r:
                l = r
                r = s.find(c, l+1)
                
        return res