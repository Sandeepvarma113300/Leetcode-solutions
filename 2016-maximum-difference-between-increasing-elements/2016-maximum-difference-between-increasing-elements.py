class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i<j and nums[i]<nums[j]:
                    res=max(res,nums[j]-nums[i])
        if res:
            return res
        else:
            return -1
