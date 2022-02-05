# Problem Link: https://leetcode.com/problems/min-stack/


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Solution I: Initial idea but with linear time, which does not meet the requirement of the problem
# Runtime: 1732 ms, faster than 5.02% of Python3 online submissions for Min Stack.
# Memory Usage: 18 MB, less than 93.94% of Python3 online submissions for Min Stack.
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min = float('inf')
        for i in self.stack:
            if i < min:
                min = i
        return min


# Solution II: Improve time complexity by maintaining an extra helper stack to keep track of the minimum elements
# Runtime: 84 ms, faster than 45.23% of Python3 online submissions for Min Stack.
# Memory Usage: 18.2 MB, less than 56.29% of Python3 online submissions for Min Stack.
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0 or val <= self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
