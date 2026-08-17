class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l < r:
            mid = l + (r - l) // 2
            currHours = 0
            for num in piles:
                currHours += (num // mid)
                if num % mid:
                    currHours += 1
            print(currHours)
            if currHours <= h:
                r = mid
            else:
                l = mid + 1
            
        
        return l
        #max k = max piles, minimum = 1
        # calculate total amt of hours taken to eat
        # if total amt is higher than h, cut in half and add
        # use a lower bound binary search


        