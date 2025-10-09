class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxii=0
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c=c+1
                maxii=max(maxii,c)
            else:
                c=0
        return maxii
    
        