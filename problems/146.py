# Problem Link: https://leetcode.com/problems/lru-cache/

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# Solution I: linked list and hash table
# Runtime: 908 ms, faster than 53.71% of Python3 online submissions for LRU Cache.
# Memory Usage: 77.2 MB, less than 5.57% of Python3 online submissions for LRU Cache.
class LinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = {}
        self.head = LinkedNode(-1, -1)
        self.tail = LinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def removeNode(self, node: LinkedNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToHead(self, node: LinkedNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def moveToHead(self, node: LinkedNode) -> None:
        self.removeNode(node)
        self.addToHead(node)
        
    def removeTail(self) -> LinkedNode:
        res = self.tail.prev
        self.removeNode(res)
        return res
            
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            newNode = LinkedNode(key, value)
            if newNode:
                self.cache[key] = newNode
                self.addToHead(newNode)
                self.size += 1
                if self.size > self.capacity:
                    removedTail = self.removeTail()
                    del self.cache[removedTail.key]
                    self.size -= 1



# Solution II: ordered dictionray
# Runtime: 772 ms, faster than 76.58% of Python3 online submissions for LRU Cache.
# Memory Usage: 75.3 MB, less than 83.31% of Python3 online submissions for LRU Cache.
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity
            
    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)