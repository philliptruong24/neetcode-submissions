class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r, c = q.popleft()       
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    grid[nr][nc] == 2 ** 31 - 1):
                    grid[nr][nc] = 1 + grid[r][c]
                    q.append((nr, nc))
        



            
