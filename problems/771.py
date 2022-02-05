# 771. Jewels and Stones
# Easy
#
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
#
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0
#
# Constraints:
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.
#
# Hint:
# For each stone, check if it is a jewel.



# Solution I:
# Runtime: 28 ms, faster than 84.72% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.1 MB, less than 74.66% of Python3 online submissions for Jewels and Stones.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        letters = {}
        for n in stones:
            if n in letters:
                letters[n] += 1
            else:
                letters[n] = 1
        result = 0
        for n in jewels:
            if n in letters:
                result += letters[n]
        return result



# Solution II:
# Runtime: 28 ms, faster than 84.72% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.3 MB, less than 46.88% of Python3 online submissions for Jewels and Stones.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        for stone in stones:
            if stone in jewels:
                result += 1
        return result



# Solution III:
# Runtime: 32 ms, faster than 61.84% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.2 MB, less than 74.66% of Python3 online submissions for Jewels and Stones.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        setJ = set(jewels)
        return sum(s in setJ for s in stones)



# Solution IV:
# https://leetcode.com/problems/jewels-and-stones/discuss/113574/1-liners-PythonJavaRuby
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
            return sum(map(jewels.count, stones))
            # return sum(map(stones.count, jewels))               # this one after seeing https://discuss.leetcode.com/post/244105
            # return sum(s in jewels for s in stones)