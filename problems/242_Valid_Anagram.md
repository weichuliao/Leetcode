Problem Link: https://leetcode.com/problems/valid-anagram/

## Solution I
hash map

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        table1, table2 = {}, {}
        for c in s:
            table1[c] = 1 + table1.get(c, 0)
        for c in t:
            table2[c] = 1 + table2.get(c, 0)
            
        for k in table1.keys():
            if k not in table2 or table1[k] != table2[k]:
                return False
        return True
```

#### Complexity Analysis:
- Time: $O(N)$ where N denotes the length of one of the input strings.
- Space: $O(N)$

<br>

## Solution II
sorting

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)
        return s == t
```

#### Complexity Analysis:
- Time: $O(NlogN)$ for sorting.
- Space: $O(1)$. Note that in Python, `sorted` makes a copy of the string, so it costs $O(N)$ extra space.