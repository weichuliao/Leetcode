# 2. Add Two Numbers
# Medium
# 
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  
# 
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution III:
# Runtime: 52 ms, faster than 99.80% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.2 MB, less than 73.33% of Python3 online submissions for Add Two Numbers.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
                
            carry, val = divmod(v1+v2+carry, 10)
            # val = (v1 + v2 + carry) % 10
            # carry = (v1 + v2 + carry) // 10
            
            n.next = ListNode(val)
            n = n.next
        return root.next





# Solution II:

# class Solution:
#     def insert(self, root=None, node=None):
#         if (root == None):
#             root = node
#         else:
#             ptr = root
#             while ptr.next != None:
#                 ptr = ptr.next
#             ptr.next = node
#         return root

#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         curNode1 = l1
#         curNode2 = l2
#         head = None
#         flag = False
        
#         while curNode1 != None or curNode2 != None:
#             sum = 0
            
#             if curNode1 != None:
#                 sum += curNode1.val
#             if curNode2 != None:
#                 sum += curNode2.val
             
#             if flag:
#                 sum += 1
#                 flag = False
#                 # print("step2-1: " + str(sum) + "\n")
                
#                 if sum >= 10:
#                     new = ListNode(sum % 10)
#                     head = self.insert(head, new)
#                     flag = True
#                 else:
#                     new = ListNode(sum)
#                     self.insert(head, new)
                    
#                 # print("step2-2: " + str(sum) + "\n")
                
#             elif sum >= 10:
#                 new = ListNode(sum % 10)
#                 head = self.insert(head, new)
#                 flag = True
#                 # print("step1: " + str(sum%10) + "\n")
                
#             else:
#                 new = ListNode(sum)
#                 head = self.insert(head, new)
#                 # print("step3: " + str(sum) + "\n")
                
#             if curNode1 != None:
#                 curNode1 = curNode1.next
#             if curNode2 != None:
#                 curNode2 = curNode2.next
            
#         if flag == True:
#             new = ListNode(1)
#             head = self.insert(head, new)
        
#         return head
        



# Solution I:
# Runtime: 72 ms, faster than 54.80% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.3 MB, less than 44.76% of Python3 online submissions for Add Two Numbers.

# class Solution:
#     def insert(self, root=None, node=None): 
#         arr1 = []
#         curNode = l1
#         nextNode = curNode.next
#         while curNode != None:
#             arr1.append(curNode.val)
#             nextNode = curNode
#             curNode = curNode.next
#         # print(arr1)
        
#         arr2 = []
#         curNode = l2
#         nextNode = curNode.next
#         while curNode != None:
#             arr2.append(curNode.val)
#             nextNode = curNode
#             curNode = curNode.next
#         # print(arr2)
        
#         num1 = 0
#         for i in range(len(arr1)):
#             num1 += arr1[i] * 10 ** i
#         # print(num1)
        
#         num2 = 0
#         for i in range(len(arr2)):
#             num2 += arr2[i] * 10 ** i
#         # print(num2)
        
#         sum = num1 + num2
#         # print(sum)
        
#         if (sum == 0):
#             return ListNode(0)
        
#         head = None
#         while sum > 0:
#             tmp = ListNode(sum % 10)
#             if head == None:
#                 head = tmp
#             else:
#                 ptr = head
#                 while (ptr.next != None):
#                     ptr = ptr.next
#                 ptr.next = tmp
#             sum //= 10
#         return head