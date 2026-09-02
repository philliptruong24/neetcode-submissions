class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            currLen = len(res)

            for i in range(currLen):
                currSubset = res[i].copy()
                currSubset.append(num)
                res.append(currSubset)
        
        return res