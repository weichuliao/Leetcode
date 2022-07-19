# Problem Link: https://leetcode.com/problems/copy-list-with-random-pointer/

## Solution I:
iterative with O(N) space

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key"
        # and new node reference as the "value"
        self.visited = {}
    
    def getClonedNode(self, node):
        # If node exists, then...
        if node:
            # Check if it's in the visited dictionary
            if node in self.visited:
                # If it's in the visited dictionary,
                # then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise, create a new node,
                # save the reference in the visited dictionary and return it
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        old_node = head
        # Create the new head node
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node
        
        # Iterate on the linked list until all nodes are cloned
        while old_node != None:
            # Get the clones of the nodes referenced by random and next pointers
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            
            # Move one step ahead in the linked list
            old_node = old_node.next
            new_node = new_node.next
        
        return self.visited[head]
```

#### Complexity Analysis:
- Time: $O(N)$ for one pass over the original linked list
- Space: $O(N)$ for a dictionary containing mapping from old list nodes to new ones

<br>

## Solution II
Iterative with O(1) space

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        # Create a new weaved list of original and copied nodes
        ptr = head
        while ptr:
            # Clone node
            new_node = Node(ptr.val, None, None)
            
            # Insert the cloned node just next to the original node
            # If A->B->C is the original linked list, 
            # linked list after weaving cloned nodes would be A->A'->B->B'->C->C'.
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        
        ptr = head
        
        # Link the random pointers of the new nodes created
        # Iterate the newly created list and use the original nodes random pointers
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        
        # Unweave the linked list to get back the original linked list and the cloned list
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head
        ptr_new_list = head.next
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
```

#### Complexity Analysis:
- Time: $O(N)$
- Space: $O(1)$