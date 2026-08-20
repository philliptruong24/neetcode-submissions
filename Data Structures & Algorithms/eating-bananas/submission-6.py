class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = l + (r- l) //2
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / mid)
            
            if hours <= h:
                r = mid
            else:
                l = mid + 1

        return l