# Problem link: https://leetcode.com/problems/design-a-stack-with-increment-operation/

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


"""
Solution I: using list to implement stack

Complexity Analysis:
- Time: O(1) for push and pop; O(min(stack_size, k)) for increment
- Space: O(1)

Runtime: 136 ms, faster than 48.02% of Python3 online submissions for Design a Stack With Increment Operation.
Memory Usage: 14.9 MB, less than 74.32% of Python3 online submissions for Design a Stack With Increment Operation.
"""
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        length = min(len(self.stack), k)
        for i in range(length):
            self.stack[i] += val



"""
Solution II: prefix sum

Complexity Analysis:
- Time: 
- Space: 

Runtime: 76 ms, faster than 95.51% of Python3 online submissions for Design a Stack With Increment Operation.
Memory Usage: 15 MB, less than 46.34% of Python3 online submissions for Design a Stack With Increment Operation.
"""
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.incre = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.incre.append(0)

    def pop(self) -> int:
        if len(self.stack) > 0:
            val = self.stack.pop()
            if len(self.stack) >= 1:
                self.incre[-2] += self.incre[-1]
            return val + self.incre.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            length = min(len(self.stack), k) - 1
            self.incre[length] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)