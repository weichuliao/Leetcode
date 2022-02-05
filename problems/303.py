# Problem Link: https://leetcode.com/problems/range-sum-query-immutable/



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)



"""
Solution I:

Complexity Analysis:
- Time: 初始化 O(n)，每次检索 O(1)，其中 n 是数组 nums 的长度。初始化需要遍历数组 nums 计算前缀和，时间复杂度是 O(n)。每次检索只需要得到两个下标处的前缀和，然后计算差值，时间复杂度是 O(1)
- Space: O(n)，其中 n 是数组 nums 的长度。需要创建一个长度为 n+1 的前缀和数组。

Runtime: 76 ms, faster than 85.99% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.6 MB, less than 78.71% of Python3 online submissions for Range Sum Query - Immutable.
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]