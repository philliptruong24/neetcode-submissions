class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n + 1):
            res = 0
            temp = i
            while temp:
                temp &= temp - 1
                res += 1
            output[i] = res
        return output