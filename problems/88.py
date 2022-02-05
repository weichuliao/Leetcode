# Problem Link: https://leetcode.com/problems/merge-sorted-array/


# Solution I: Initial Idea
# Runtime: 36 ms, faster than 77.91% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14.4 MB, less than 30.06% of Python3 online submissions for Merge Sorted Array.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i, n in enumerate(nums2):
                nums1[i] = n
            return
        if n == 0:
            return
        
        nums_copy = nums1.copy()
        count1, count2, count3 = 0, 0, 0
        num1, num2 = nums1[count1], nums2[count2]
        while m > 0 and n > 0:
            if num1 == None and m > 0:
                count1 += 1
                num1 = nums_copy[count1]
            if num2 == None and n > 0:
                count2 += 1
                num2 = nums2[count2]
            if num1 <= num2:
                nums1[count3] = num1
                m -= 1
                num1 = None
            else:
                nums1[count3] = num2
                n -= 1
                num2 = None
            count3 += 1
        
        if (m > 0):
            for i in range(m):
                nums1[count3] = nums_copy[count1]
                count1 += 1
                count3 += 1
        elif (n > 0):
            for i in range(n):
                nums1[count3] = nums2[count2]
                count2 += 1
                count3 += 1


"""
Solution II: Combine array then sorting

Runtime: 59 ms, faster than 16.63% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.3 MB, less than 61.00% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        # Sort nums1 list in-place.
        nums1.sort()



"""
Solution III: Two pointers

Runtime: 40 ms, faster than 52.29% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.5 MB, less than 30.06% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] <= nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted



"""
Solution IV: Append from tail

Runtime: 28 ms, faster than 98.20% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.3 MB, less than 30.17% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] >= nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[length] = nums1[m]
                length -= 1
                m -= 1
            else:
                nums1[length] = nums2[n]
                length -= 1
                n -= 1
        while m >= 0:
            nums1[length] = nums1[m]
            length -= 1
            m -= 1
        while n >= 0:
            nums1[length] = nums2[n]
            length -= 1
            n -= 1