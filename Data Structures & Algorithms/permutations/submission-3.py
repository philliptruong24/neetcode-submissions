class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = set()

        def dfs(i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for j in range(0, len(nums)):
                if j in used:
                    continue

                curr.append(nums[j])
                used.add(j)

                dfs(i + 1)

                curr.pop()
                used.remove(j)

        dfs(0)
        return res