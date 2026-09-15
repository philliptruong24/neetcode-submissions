
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = defaultdict(Node)
        def dfs(n):
            if n is None:
                return
            if n in nodeMap:
                return nodeMap[n]
            if n not in nodeMap:
                nodeMap[n] = Node(n.val, [])
            
            for neighbor in n.neighbors:
                nodeMap[n].neighbors.append(dfs(neighbor))

            return nodeMap[n]
    
        return dfs(node)

