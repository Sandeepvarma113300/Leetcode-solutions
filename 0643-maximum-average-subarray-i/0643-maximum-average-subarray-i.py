class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=sum(nums[:k])
        max_avg=window
        for i in range(k,len(nums)):
            window=(window-nums[i-k]+nums[i])
            max_avg=max(window,max_avg)
        return max_avg/k
