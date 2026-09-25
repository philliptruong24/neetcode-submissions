"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}
        def dfs(n):
            if n in clone:
                return clone[n]
            
            clone[n] = Node(n.val)

            for nei in n.neighbors:
                clone[n].neighbors.append(dfs(nei))
            
            return clone[n]
        
        return dfs(node) if node else None

        