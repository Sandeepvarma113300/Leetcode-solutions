class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        s=0
        if len(nums)<=1:
            return nums[0]
        for i in range(len(nums)):
            if i%2==0:
                s=s+nums[i]
            else:
                s=s-nums[i]
        return s