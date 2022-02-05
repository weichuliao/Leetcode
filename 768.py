# Problem Link: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

"""
Solution I: counting

Complexity Analysis:
- Time: O(NlogN) mainly for sorting
- Space: O(N) for using a counter, where N denotes the length of list

Runtime: 110 ms, faster than 25.67% of Python3 online submissions for Max Chunks To Make Sorted II.
Memory Usage: 14.7 MB, less than 50.98% of Python3 online submissions for Max Chunks To Make Sorted II.
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Complexity Analysis:
        - Time: O(N) for comparison between count_a and count_b
        - Space: O(N) for 2 counters used and size of each is N
        
            for a, b in zip(arr, sorted(arr)):
                count_a[a] += 1
                count_b[b] += 1
                if count_a == count_b: ans += 1
            return ans

        Improved vesion as below:
        """
        count = collections.defaultdict(int)
        non_zero_cnt = 0
        ans = 0
        for a, b in zip(arr, sorted(arr)):
            if count[a] == -1: non_zero_cnt -= 1
            if count[a] == 0: non_zero_cnt += 1
            count[a] += 1
            if count[b] == 1: non_zero_cnt -= 1
            if count[b] == 0: non_zero_cnt += 1
            count[b] -= 1
            if non_zero_cnt == 0: ans += 1
        return ans



"""
Solution II: monotonous stack

Complexity Analysis:
- Time: O(N) where N denotes the length of input list
- Space: O(N) where N denotes the length of chunks

Runtime: 72 ms, faster than 78.25% of Python3 online submissions for Max Chunks To Make Sorted II.
Memory Usage: 14.7 MB, less than 17.47% of Python3 online submissions for Max Chunks To Make Sorted II.
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for a in arr:
            if stack and stack[-1] > a:
                cur = stack[-1]
                while stack and stack[-1] > a: stack.pop()
                stack.append(cur)
            else:
                stack.append(a)
        return len(stack)