Problem Link: https://leetcode.com/problems/implement-trie-prefix-tree/

## Solution I

```python
class Trie:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                # if word > trie
                return False
        return True if cur.isWord else False

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

#### Complexity Analysis:
- Time:
    - Insertion: $O(m)$ where m is the key length
    - Search for a key: $O(m)$
    - Search for a key prefix: $O(m)$
- Space:
    - Insertion: $O(m)$ in worst case the key doesn't share prefix with other keys
    - Search for a key: $O(1)$
    - Search for a key prefix: $O(1)$