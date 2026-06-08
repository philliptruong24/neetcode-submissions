class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        seen = set()
        while n > 1:
            for digit in str(n):
                total += int(digit) ** 2
            if total in seen:
                return False
            else:
                seen.add(total)
            n = total
            total = 0
        return True