class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, 0) and len(visited) == n
