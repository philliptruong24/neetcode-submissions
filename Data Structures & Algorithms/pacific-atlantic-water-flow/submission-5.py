class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, visitSet, prevHeight):
            if ((r, c) in visitSet or
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return
            
            visitSet.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, visitSet, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        res = []
        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r,c])

        return res


