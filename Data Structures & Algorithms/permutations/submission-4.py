class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = set()

        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for j in range(0, len(nums)):
                if j in used:
                    continue

                curr.append(nums[j])
                used.add(j)

                dfs()

                curr.pop()
                used.remove(j)

        dfs()
        return res