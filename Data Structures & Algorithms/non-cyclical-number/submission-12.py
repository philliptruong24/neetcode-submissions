class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            seen.add(n)
            n = self.sumOfSquares(n)
            if n in seen:
                return False
        return True

    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = (n % 10) ** 2
            output += digit
            n = n // 10
        return output
