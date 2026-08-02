class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        i = 0
        j = len(numbers) - 1
        while i < j:
            diff = numbers[i] + numbers[j]
            if diff == target:
                return [i + 1, j + 1]
            elif diff > target:
                j -= 1
            else:
                i += 1
    
        
