Problem Link: 

## Solution I
hash map and sorting

```python
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Find for every user separately the websites he visited
        mapping = defaultdict(list)
        for time, username, web in sorted(zip(timestamp, username, website)):
            mapping[username].append(web)
        
        # Consider all possible 3-sequences, 
        # find the number of distinct users who visited each of them
        counter = defaultdict(int)
        for websiteList in mapping.values():
            combs = set(combinations(websiteList, 3))
            for comb in combs:
                counter[comb] += 1
        
        # Sort the counter descendingly by value, then lexicographically
        result = sorted(counter, key=lambda x: (-counter[x], x))
        return result[0]
```

#### Complexity Analysis:
- Time: $$ It will take O(n C r) to get 1 combination, and for getting r combinations, it is O(r). Hence, the total time complexity is O( r * [nCr]).
- Space: $$