# Problem Link: https://leetcode.com/problems/insert-delete-getrandom-o1/

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


"""
Solution I: initial idea

Runtime: 1028 ms, faster than 9.17% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 62.1 MB, less than 14.27% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
class RandomizedSet:

    def __init__(self):
        self.list = []

    def insert(self, val: int) -> bool:
        tmp = set(self.list)
        if val not in tmp:
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        tmp = set(self.list)
        if val in tmp:
            self.list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)


"""
Solution II: list and hash table

Runtime: 440 ms, faster than 75.30% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 61.9 MB, less than 26.31% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
class RandomizedSet:

    def __init__(self):
        self.list = []
        self.hash_table = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if val not in self.hash_table:
            self.list.append(val)
            self.length += 1
            self.hash_table[val] = self.length - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hash_table:
            target_idx = self.hash_table[val]
            last_element = self.list[-1]
            self.list[-1] = val
            self.list[target_idx] = last_element
            self.hash_table[last_element] = target_idx
            self.hash_table[val] = self.length - 1
            self.list.pop()
            del self.hash_table[val]
            self.length -= 1
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)

"""
Slightly Revised Solution II:

Runtime: 444 ms, faster than 73.92% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 61.9 MB, less than 26.31% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
class RandomizedSet:

    def __init__(self):
        self.list = []
        self.hash_table = {}

    def insert(self, val: int) -> bool:
        if val not in self.hash_table:
            self.list.append(val)
            self.hash_table[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hash_table:
            idx, last_element = self.hash_table[val], self.list[-1]
            self.list[idx], self.hash_table[last_element] = last_element, idx
            self.list.pop()
            del self.hash_table[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)