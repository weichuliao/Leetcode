# Problem Link: https://leetcode.com/problems/design-hashmap/



"""
Solution I: 

Complexity Analysis:
- Time: O(N/K)
- Space: O(K+M)

Runtime: 527 ms, faster than 29.34% of Python3 online submissions for Design HashMap.
Memory Usage: 18.3 MB, less than 24.37% of Python3 online submissions for Design HashMap.
"""
class Bucket:
    
    def __init__(self):
        self.bucket = []
    
    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
    
class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)