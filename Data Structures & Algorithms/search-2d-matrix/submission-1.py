class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        while i > -1:
            if matrix[i][0] <= target:
                break
            i -= 1
        
        if i == -1:
            return False
        
        for digit in matrix[i]:
            if digit == target:
                return True
        
        return False