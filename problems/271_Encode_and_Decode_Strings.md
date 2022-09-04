Problem Link: https://leetcode.com/problems/encode-and-decode-strings/

## Solution I
length of strings + characters as delimiters

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res, start = [], 0
        while start < len(s):
            end = start
            while s[end] != '#':
                end += 1
            length = int(s[start:end])  # not including end
            res.append(s[end+1:end+1+length])
            start = end + 1 + length
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

#### Complexity Analysis:
- Time: $O(N)$ for both encoding and decoding.
- Space:
  - Encode: $O(1)$ for keeping one output string.
  - Decode: $O(N)$ for keeping one output array of strings.

<br>

## Solution II
chunked transfer encoding

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        def len_to_str(x):
            x = len(x)
            bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
            bytes.reverse()
            bytes_str = ''.join(bytes)
            return bytes_str
        
        ans = ''.join(len_to_str(x) + x for x in strs)
        return ans

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        def str_to_int(s):
            result = 0
            for ch in s:
                result = result * 256 + ord(ch)
            return result
            
        i, n = 0, len(s)
        output = []
        while i < n:
            length = str_to_int(s[i:i+4])
            i += 4
            output.append(s[i:i+length])
            i += length
        return output

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

#### Complexity Analysis:
- Time: $O(N)$ for both encoding and decoding.
- Space:
  - Encode: $O(1)$ for keeping one output string.
  - Decode: $O(N)$ for keeping one output array of strings.