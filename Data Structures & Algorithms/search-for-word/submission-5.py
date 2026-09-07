class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        flag = False
        totalRows = len(board)
        totalCols = len(board[0])

        def dfs(idx, row, col):
            if idx == len(word):
                return True
            
            elif (row < 0 or row == totalRows
                or col < 0 or col == totalCols
                or (row, col) in seen
                or board[row][col] != word[idx]):
                return False
            
            else:
                seen.add((row, col))
                idx += 1
                down = dfs(idx, row + 1, col)
                up = dfs(idx, row - 1, col)
                right = dfs(idx, row, col + 1)
                left = dfs(idx, row, col - 1)

                seen.remove((row, col))
                return up or down or left or right
            

        for row in range(totalRows):
            for col in range(totalCols):
                if board[row][col] == word[0]:
                    flag = flag or dfs(0, row, col)
    
        return flag

