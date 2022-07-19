Problem Link: https://leetcode.com/problems/design-in-memory-file-system/

## Solution I
Trie - a tree-like data structure which is commonly used to represent a dictionary for looking up words in a vocabulary. Each node represents a single character of a given string.

examples: [was, wax, what]

root
 |-- w
     |-- a
     |   |-- s (was)
     |   |-- x (wax)
     |
     |-- h
         |-- a
             |-- t (what)

- node value: character -> file or directory name
- leaf node: an end of string -> a file

```python
class TrieNode:
    def __init__(self):
        self.content = ""
        self.children = defaultdict(TrieNode)
        self.isfile = False
        
class FileSystem:

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        # path_list = path.split("/")
        # node = self.root
        # for p in path_list:
        #     g
        #     node = node.children.get(p)
        # if node.isfile: return [p]
        node = self._traverse(path, True)
        if node.isfile: return [path.split("/")[-1]]
        
        ans = [i for i in node.children.keys()]
        return sorted(ans) if ans else ans

    def mkdir(self, path: str) -> None:
        # path_list = path.split("/")
        # node = self.root
        # for p in path_list:
        #     if not p: continue
        #     node = node.children[p]
        self._traverse(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        # path_list = filePath.split("/")
        # node = self.root
        # for p in path_list:
        #     if not p: continue
        #     node = node.children[p]
        node = self._traverse(filePath, False)
        node.content += content
        node.isfile = True

    def readContentFromFile(self, filePath: str) -> str:
        # path_list = filePath.split("/")
        # node = self.root
        # for p in path_list:
        #     if not p: continue
        #     node = node.children.get(p)
        node = self._traverse(filePath, True)
        return node.content
    
    def _traverse(self, path: str, travel: bool) -> TrieNode:
        path_list = path.split("/")
        node = self.root
        for p in path_list:
            if not p: continue  # deal with empty
            node = node.children.get(p) if travel else node.children[p]
        return node


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
```

#### Complexity Analysis:
- Time: $$
- Space: $$