class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l=0
        for i in range(1,len(nums)):
            if nums[l]==nums[i]:
                nums[l]*=2
                nums[i]=0
            l=l+1
        p=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[p],nums[i]=nums[i],nums[p]
                p+=1
        return nums
        