# Problem Link: https://leetcode.com/problems/third-maximum-number/

"""
Solution I: sort and then traverse the list to find the third maximum number, while using a counter variable to count

Complexity Analysis:
- Time: O(NlogN) for sorting + O(N) for traversal over the array
- Space: O(logN) 排序需要的棧空間為 O(logn)

Runtime: 48 ms, faster than 89.62% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.8 MB, less than 95.05% of Python3 online submissions for Third Maximum Number.
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        third_max = nums[0]
        counter = 1
        for i in nums:
            if counter >= 3:
                break
            if i < third_max:
                third_max = i
                counter += 1
        if counter < 3:
            return nums[0]
        else:
            return third_max



"""
Solution II: sorting

Runtime: 52 ms, faster than 76.63% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.8 MB, less than 84.08% of Python3 online submissions for Third Maximum Number.
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        diff = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                diff += 1
                if diff == 3:  # 此时 nums[i] 就是第三大的数
                    return nums[i]
        return nums[0]



"""
Solution III: sorted list

Complexity Analysis:
- Time: O(n) where n denotes the length of nums. 由於有序集合的大小至多為 3，插入和刪除的時間複雜度可以視作是 O(1) 的，因此時間複雜度為 O(n)
- Space: O(1)

Runtime: 115 ms, faster than 5.88% of Python3 online submissions for Third Maximum Number.
Memory Usage: 15.3 MB, less than 50.49% of Python3 online submissions for Third Maximum Number.
"""
from sortedcontainers import SortedList

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = SortedList()
        for num in nums:
            if num not in s:
                s.add(num)
                if len(s) > 3:
                    s.pop(0)
        return s[0] if len(s) == 3 else s[-1]



"""
Solution IV: traverse once and maintain three variables to keep the first three maximum numbers

Complexity Analysis:
- Time: O(n) where n denotes the length of nums
- Space: O(1) for only three integer variables

Runtime: 68 ms, faster than 31.31% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.8 MB, less than 83.97% of Python3 online submissions for Third Maximum Number.
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif a > num > b:
                b, c = num, b
            elif b > num > c:
                c = num
        return a if c == float('-inf') else c
        
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = None, None, None
        for num in nums:
            if a is None or num > a:
                a, b, c = num, a, b
            elif a > num and (b is None or num > b):
                b, c = num, b
            elif b is not None and b > num and (c is None or num > c):
                c = num
        return a if c is None else c