# Initial idea but wrong answer
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        count = 0
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                if count > 2:
                    return False
                else:
                    diff.append((s[i], goal[i]))
        if count == 0:
            if s[0] == s[1]:
                return True
            return False
        s1, g1 = diff[0]
        s2, g2 = diff[1]
        if s1 == g1 and s2 == g2:
            return True
        elif s1 == g2 and s2 == g1:
            return True
        elif s1 == s2:
            return True
        else:
            return False


# Solution I: 情況列舉
# Runtime: 46 ms, faster than 31.67% of Python3 online submissions for Buddy Strings.
# Memory Usage: 14.6 MB, less than 11.90% of Python3 online submissions for Buddy Strings.
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False
        else:
            pairs = []
            for a, b in zip(s, goal):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3:
                    return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1] # pairs[1][::-1] results in the reverse of pairs[1]