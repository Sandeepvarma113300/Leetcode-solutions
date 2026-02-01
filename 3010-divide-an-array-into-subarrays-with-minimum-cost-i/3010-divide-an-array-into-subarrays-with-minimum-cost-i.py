class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        c = float('inf')
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                cost = nums[0] + nums[i] + nums[j]
                c = min(c, cost)
        return c
