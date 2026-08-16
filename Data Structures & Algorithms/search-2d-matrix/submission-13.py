class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
       
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                l2 = 0
                r2 = len(matrix[mid]) - 1
                while l2 <= r2:
                    mid2 = l2 + (r2 - l2) // 2
                    if matrix[mid][mid2] == target:
                        return True
                    
                    elif matrix[mid][mid2] < target:
                        l2 = mid2 + 1
                    else:
                        r2 = mid2 - 1
                break
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
        
            