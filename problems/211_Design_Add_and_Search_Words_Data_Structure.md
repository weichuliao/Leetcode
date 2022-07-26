Problem Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

## Solution I

```python
sys.setrecursionlimit(10**6)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        # DFS to deal with word starting with "."
        def searchNode(word, node):
            for i, c in enumerate(word):
                if c == ".":
                    for x in node.children.values():
                        if searchNode(word[i+1:], x):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.isWord
        return searchNode(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

#### Complexity Analysis:
- Time:
    - Add word: $O(M)$ where M is the key length.
    - Search: $O(M)$ for the "well-defined" words without dots, where M is the key length, and N is a number of keys, and $O(N⋅26^M)$ for the "undefined" words.
- Space:
    - Add word: $O(M)$. In worst case, the newly inserted key doesn't share a prefix with other keys, so we have to add M new nodes, which takes O(M) space.
    - Search: $O(1)$ for the search of "well-defined" words without dots, and up to $O(M)$ for the "undefined" words, to keep the recursion stack.