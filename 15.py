# Runtime: 6959 ms
# Memory Usage: 18.2 MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return
        
        nums.sort(reverse=True)
        
        output = []
        for i in range(len(nums)):
            fix_rest = 0 - nums[i]
            hash_map = {}
            for j in range(i+1, len(nums)):
                target = fix_rest - nums[j]
                if target in hash_map:
                    temp = [nums[j], target, nums[i]]
                    if temp not in output:
                        output.append(temp)
                else:
                    hash_map[nums[j]] = j
        return output



# Runtime: 3360 ms, faster than 24.04% of Python3 online submissions for 3Sum.
# Memory Usage: 18.2 MB, less than 19.26% of Python3 online submissions for 3Sum.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return
        
        nums.sort()
        
        output = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            fix_rest = 0 - nums[i]
            hash_map = {}
            for j in range(i+1, len(nums)):
                target = fix_rest - nums[j]
                if target in hash_map:
                    temp = [nums[i], target, nums[j]]
                    if temp not in output:
                        output.append(temp)
                else:
                    hash_map[nums[j]] = nums[j]
        return output



# Runtime: 899 ms, faster than 66.14% of Python3 online submissions for 3Sum.
# Memory Usage: 16.8 MB, less than 99.68% of Python3 online submissions for 3Sum.
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res



# Runtime: 960 ms, faster than 59.65% of Python3 online submissions for 3Sum.
# Memory Usage: 18 MB, less than 29.30% of Python3 online submissions for 3Sum.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res