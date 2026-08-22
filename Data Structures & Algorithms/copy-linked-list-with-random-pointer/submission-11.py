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
        
        copy = {None:None}
        curr = head
        while curr:
            copy[curr] = Node(curr.val, curr.next, curr.random)
            curr = curr.next
        
        curr = copy[head]
 
        while curr:
            if curr.next:
                curr.next = copy[curr.next]
            if curr.random:
                curr.random = copy[curr.random]
            curr = curr.next        
        
        return copy[head]
        
        