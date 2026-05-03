class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in counter:
                return [counter[diff], i]
            counter[n] = i
