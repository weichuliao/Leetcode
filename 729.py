# Problem Link: https://leetcode.com/problems/my-calendar-i/

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



# Solution I: not accepted
class Event:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end
        self.prev = None
        self.next = None
    
class MyCalendar:

    def __init__(self):
        self.head = Event()
        self.tail = Event()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def addToHead(self, node):
        nextNode = self.head.next
        self.head.next = node
        nextNode.prev = node

    def book(self, start: int, end: int) -> bool:
        if start >= self.tail.prev.end:
            newNode = Event(start, end)
            prevNode = self.tail.prev
            prevNode.next = newNode
            newNode.prev = prevNode
            return True
        return False



"""
Solution II: brute force

Complexity Analysis:
- Time: O(N^2) where N is the number of events booked. For each new event, we process every previous event to decide whether the new event can be booked. This leads to ∑ k to N (O(k)) = O(N^2) complexity.
- Sapce: O(N), the size of the calendar.

Runtime: 676 ms, faster than 29.84% of Python3 online submissions for My Calendar I.
Memory Usage: 14.7 MB, less than 94.93% of Python3 online submissions for My Calendar I.
"""
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True



"""
Solution III: binary search tree

Complexity Analysis:
- Time: O(N^2) worst case, with O(NlogN) on random data. For each new event, we insert the event into our binary tree. As this tree may not be balanced, it may take a linear number of steps to add each event.
- Space: O(N) where N denotes the size of the calendar

Runtime: 260 ms, faster than 79.30% of Python3 online submissions for My Calendar I.
Memory Usage: 14.9 MB, less than 75.06% of Python3 online submissions for My Calendar I.
"""
class Node:
    
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = self.right = None
        
    def insert(self, node) -> bool:
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False
        
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))