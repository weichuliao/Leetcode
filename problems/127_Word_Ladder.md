Problem Link: https://leetcode.com/problems/word-ladder/

## Solution I
O(n*m^2) for BFS where n is the length of wordList and m is the length of a particular word

O(n*m^2) for creating adjacency list: use pattern as the key and word fitting that pattern as the value
the number of edges will be 'n' not 'n^2'. Your BFS will still be O(n*m^2) (same as creating hashtable): m for getting the pattern and there are total of m patterns

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        # Dictionary to hold combination of words that can be formed from any given word
        # By changing one letter at a time
        neighbor = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                # Key is the pattern
                # Value is a list of words which share the same pattern
                pattern = word[:j] + "*" + word[j+1:]
                neighbor[pattern].append(word)
        
        # Queue for BFS
        q = deque([beginWord])
        # Set to make sure not to re-visit the same word
        visit = set([beginWord])
        # Hold the answer of the problem: the level number of a node
        # At least one word along the path
        res = 1
        while q:
            # Going through the entire layer until the queue is empty
            for i in range(len(q)):
                curWord = q.popleft()
                if curWord == endWord:
                    return res
                # Take the neighbors of curWord and add them to the queue
                for j in range(len(curWord)):
                    # All the patterns that curWord falls into
                    # And get all the words that fall into the same pattern
                    pattern = curWord[:j] + "*" + curWord[j+1:]
                    for neiWord in neighbor[pattern]:
                        # Make sure we don't get the same word twice
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
            
        return 0
```

#### Complexity Analysis:
- Time: $O(M*N^2)$ where M is the length of each word and N is the length of `wordList`
- Space: $$