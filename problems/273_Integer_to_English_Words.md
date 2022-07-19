Problem Link: https://leetcode.com/problems/integer-to-english-words/

## Solution I
divide and conquer

```python
# wrong answer (570 / 601 cases passed)
class Solution:
    def numberToWords(self, num: int) -> str:
        def getRanges(i):
            ranges = ["", "Thousand", "Million", "Billion"]
            return ranges[i]
        
        def getDigits(i):
            digits = [
                "", "One", "Two", "Three", "Four", "Five", 
                "Six", "Seven", "Eight", "Nine", "Ten", 
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
                "Sixteen", "Seventeen", "Eighteen", "Nineteen"
            ]
            return digits[i]
        
        def getTwoDigits(i):
            twoDigits = [
                "", "", "Twenty", "Thirty", "Forty", "Fifty", 
                "Sixty", "Seventy", "Eighty", "Ninety"
            ]
            return twoDigits[i]
        
        def getThreeDigits(n):
            if not n: return ""
            
            hundred = n // 100
            n %= 100
            
            if hundred and not n:
                return getDigits(hundred) + " Hundred"
            elif hundred and 1 <= n < 20:
                return getDigits(hundred) + " Hundred " + getDigits(n)
            elif hundred and 20 <= n < 100:
                ten = n // 10
                n %= 10
                result = " " + getDigits(hundred) + " Hundred " + getTwoDigits(ten)
                result += " " + getDigits(n)
                return result
            elif not hundred and 1 <= n < 20:
                return " " + getDigits(n)
            elif not hundred and 20 <= n < 100:
                ten = n // 10
                n %= 10
                result = " " + getTwoDigits(ten)
                result += " " + getDigits(n)
                return result
        
        if num == 0: return "Zero"
        
        # 按千位數切割數字
        stack = []
        while num > 0:
            stack.append(num % 1000)
            num //= 1000
        
        ans = ""
        for i in range(len(stack) - 1, -1, -1):
            temp = getThreeDigits(stack[i])
            if temp: ans += temp + " " + getRanges(i)
        return ans.strip()  # strip() takes O(N)
```

#### Complexity Analysis:
- Time: $$
- Space: $$

<br>

## Solution II
divide and conquer

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        def one(n):
            switcher = {
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine"
            }
            return switcher.get(n)
        
        def twoLess20(n):
            switcher = {
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen"
            }
            return switcher.get(n)
        
        def ten(n):
            switcher = {
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety"
            }
            return switcher.get(n)
        
        def two(n):
            if not n:
                return ""
            elif n < 10:
                return one(n)
            elif n < 20:
                return twoLess20(n)
            else:
                tenner = n // 10
                rest = n - tenner * 10
                return ten(tenner) + " " + one(rest) if rest else ten(tenner)
        
        def three(n):
            hundred = n // 100
            rest = n - hundred * 100
            if hundred and rest:
                return one(hundred) + " Hundred " + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + " Hundred"
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        if not num:
            return "Zero"
        result = ""
        if billion:
            result = " ".join((three(billion), "Billion"))
        if million:
            result = " ".join((result, three(million), "Million")) 
        if thousand:
            result = " ".join((result, three(thousand), "Thousand"))
        if rest:
            result = " ".join((result, three(rest)))
        return result.strip()  # strip() takes O(n)
```

#### Complexity Analysis:
- Time: $O(N)$
- Space: $O(1)$