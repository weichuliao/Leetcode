# Problem Link: https://leetcode.com/problems/validate-stack-sequences/


"""
Solution I: Initial idea -> Simulation with 2 pointers

Runtime: 77 ms, faster than 47.98% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 14.5 MB, less than 56.05% of Python3 online submissions for Validate Stack Sequences.
"""
class Solution:
    def validateStackSequences(self, push: List[int], pop: List[int]) -> bool:
        ptr1, ptr2, length, stack = 0, 0, len(push), []
        while ptr1 < length and ptr2 < length:
            if stack and stack[-1] == pop[ptr2]:
                stack.pop()
                ptr2 += 1
            elif push[ptr1] != pop[ptr2]:
                stack.append(push[ptr1])
                ptr1 += 1
            elif push[ptr1] == pop[ptr2]:
                if stack and stack[-1] == push[ptr1]:
                    stack.pop()
                ptr1 += 1
                ptr2 += 1
            else:
                stack.append(push[ptr1])
                ptr1 += 1
                
        while ptr2 < length:
            if pop[ptr2] == stack[-1]:
                stack.pop()
                ptr2 += 1
            else:
                return False
        return True


"""
Solution II: Greedy

Runtime: 68 ms, faster than 83.10% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 14.7 MB, less than 28.45% of Python3 online submissions for Validate Stack Sequences.
"""
class Solution:
    def validateStackSequences(self, push: List[int], pop: List[int]) -> bool:
        ptr, stack = 0, []
        for i in push:
            stack.append(i)
            while stack and ptr < len(pop) and stack[-1] == pop[ptr]:
                stack.pop()
                ptr += 1
        return ptr == len(pop)