class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)


        buckets = [[] for _ in range(len(nums) + 1)]

        for i, f in freq.items():
            buckets[f].append(i)

        res = []
        for i in range(len(buckets) - 1, 0,- 1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

