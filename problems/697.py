# Problem Link: https://leetcode.com/problems/degree-of-an-array/



"""
Solution I: left and right index

Complexity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 384 ms, faster than 34.93% of Python3 online submissions for Degree of an Array.
Memory Usage: 15.3 MB, less than 92.19% of Python3 online submissions for Degree of an Array.
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans
"""
slightly revised

Runtime: 453 ms, faster than 23.87% of Python3 online submissions for Degree of an Array.
Memory Usage: 15.9 MB, less than 25.28% of Python3 online submissions for Degree of an Array.
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = collections.defaultdict(Degree)
        for i, num in enumerate(nums):
            if num not in d:
                d[num].start = i
            d[num].end = i
            d[num].count +=1
        m = max(d.values(), key=lambda x: x.count).count
        l = [x for x in d.values() if x.count == m]
        x = min(l, key=lambda x: x.end - x.start)
        return x.end - x.start + 1

class Degree:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0



"""
Solution II: hash

Complexity Analysis:
- Time: 
- Space: 


"""




"""
Solution III: sliding window?

Complexity Analysis:
- Time: 
- Space: 


"""
