
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}
        def dfs(n):
            if n in nodeMap:
                return nodeMap[n]

            nodeMap[n] = Node(n.val)
            for neighbor in n.neighbors:
                nodeMap[n].neighbors.append(dfs(neighbor))

            return nodeMap[n]
    
        return dfs(node) if node else None

