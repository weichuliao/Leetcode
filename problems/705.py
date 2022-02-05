# Problem Link: https://leetcode.com/problems/design-hashset/



"""
Solution I: linked list as bucket

Complexity Analysis:
- Time: O(N/K)
- Space: O(K+M)

Runtime: 250 ms, faster than 59.97% of Python3 online submissions for Design HashSet.
Memory Usage: 20.4 MB, less than 22.92% of Python3 online submissions for Design HashSet.
"""
class MyHashSet:

    def __init__(self):
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
    
    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

class Node:

    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode

class Bucket:

    def __init__(self):
        self.head = Node(0)

    def insert(self, newValue):
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            
    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



"""
Solution I: binary search tree as bucket

Complexity Analysis:
- Time: 
- Space: 


"""