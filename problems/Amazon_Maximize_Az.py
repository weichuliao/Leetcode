class Solution:
    def maximizeAZ(self, s: str) -> int:
        plusA = 'A' + s
        plusZ = s + 'Z'
        countA = countZ = sumA = sumZ = 0

        for i in range(len(s) + 1):
            if plusA[i] == 'A':
                countA += 1
            elif plusA[i] == 'Z':
                sumA += countA

            if plusZ[i] == 'A':
                countZ += 1
            elif plusZ[i] == 'Z':
                sumZ += countZ
                
        return max(sumA, sumZ)

execution = Solution()
assert execution.maximizeAZ('AKZ') == 2
assert execution.maximizeAZ('BAZAZ') == 5
assert execution.maximizeAZ('AAA') == 3
assert execution.maximizeAZ('ZZZZ') == 4