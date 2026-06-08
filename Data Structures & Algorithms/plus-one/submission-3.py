class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        
        for i in range(len(digits)):
            total += digits[i] * 10 ** (len(digits) - i - 1)
        total += 1

        arr = []
        for i in str(total):
            arr.append(i)
        return arr


        