class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l=0
        for i in range(1,len(nums)):
            if nums[l]==nums[i]:
                nums[l]*=2
                nums[i]=0
            l=l+1
        b=nums
        p=0
        for i in range(len(b)):
            if b[i]!=0:
                b[p],b[i]=b[i],b[p]
                p+=1
        return b
        